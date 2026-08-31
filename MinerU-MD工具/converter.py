#!/usr/bin/env python3
"""MinerU 转 Markdown 核心转换模块。

支持：
- MinerU 云 API（PDF / PPTX / 图片等）
- MinerU 本地 pipeline
- pdftocairo + Tesseract OCR 兜底
- 自动 frontmatter
- 转换后清理（CJK 空格、Unicode 数学斜体、LaTeX 残留）
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# 允许从知识库 scripts 目录调用现有脚本
SCRIPTS_DIR = Path(r"D:\知识库\scripts")
DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

# 常见支持的文件扩展名
SUPPORTED_EXTS = {
    ".pdf",
    ".pptx", ".ppt",
    ".docx", ".doc",
    ".xlsx", ".xls",
    ".html", ".htm",
    ".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp",
}


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> dict:
    if Path(path).exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def default_config() -> dict:
    return {
        "mineru_api_token": "",
        "mineru_api_url": "https://mineru.net/api/v4",
        "mineru_model_version": "vlm",
        "mineru_command": "mineru",
        "mineru_backend": "pipeline",
        "mineru_lang": "ch",
        "tesseract_path": r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        "pdftocairo_command": "pdftocairo",
        "default_output_dir": r"D:\知识库\课程",
    }


# ============================================================
# Unicode 数学斜体 → ASCII/希腊字母
# ============================================================
def build_math_unicode_table():
    table = {}
    for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
        table[0x1D44E + i] = ch
    for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        table[0x1D434 + i] = ch
    for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
        table[0x1D482 + i] = ch
    for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        table[0x1D468 + i] = ch
    greek_map = {
        0x1D6FC: "α", 0x1D6FD: "β", 0x1D6FE: "γ", 0x1D6FF: "δ",
        0x1D700: "ε", 0x1D701: "ζ", 0x1D702: "η", 0x1D703: "θ",
        0x1D704: "ι", 0x1D705: "κ", 0x1D706: "λ", 0x1D707: "μ",
        0x1D708: "ν", 0x1D709: "ξ", 0x1D70B: "π", 0x1D70C: "ρ",
        0x1D70D: "σ", 0x1D70E: "ς", 0x1D70F: "τ", 0x1D710: "υ",
        0x1D711: "φ", 0x1D712: "χ", 0x1D713: "ψ", 0x1D714: "ω",
        0x1D71B: "Δ", 0x1D71E: "Ξ",
    }
    for cp, ch in greek_map.items():
        table[cp] = ch
    return table


MATH_TABLE = build_math_unicode_table()


def fix_math_unicode(text: str) -> str:
    result = []
    for ch in text:
        cp = ord(ch)
        if 0x1D400 <= cp <= 0x1D7FF:
            mapped = MATH_TABLE.get(cp, "")
            if mapped:
                result.append(mapped)
        else:
            result.append(ch)
    return "".join(result)


def fix_cjk_spaces(text: str) -> str:
    return re.sub(r"(?<=[一-鿿㐀-䶿])\s+(?=[一-鿿㐀-䶿])", "", text)


def fix_damaged_latex(text: str) -> str:
    text = text.replace("\\c\\dots", "\\cdots")
    text = text.replace("\\v\\dots", "\\vdots")
    text = text.replace("\\d\\dots", "\\ddots")
    return text


# ============================================================
# 文件发现
# ============================================================
def is_supported(path: str | Path) -> bool:
    return Path(path).suffix.lower() in SUPPORTED_EXTS


def collect_files(paths: list[str | Path]) -> list[Path]:
    """收集文件；如果传入目录则递归查找支持的格式。"""
    files: list[Path] = []
    seen: set[Path] = set()

    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.rglob("*")):
                if f.is_file() and is_supported(f):
                    if f not in seen:
                        files.append(f)
                        seen.add(f)
        elif path.is_file() and is_supported(path):
            if path not in seen:
                files.append(path)
                seen.add(path)
    return files


# ============================================================
# 转换器
# ============================================================
class Converter:
    def __init__(
        self,
        config: dict | None = None,
        log_callback=None,
        progress_callback=None,
    ):
        cfg = default_config()
        cfg.update(config or {})
        self.config = cfg
        self.log_callback = log_callback or (lambda msg: None)
        self.progress_callback = progress_callback or (lambda value: None)

    def log(self, msg: str):
        if callable(self.log_callback):
            self.log_callback(msg)

    def progress(self, value: int):
        if callable(self.progress_callback):
            self.progress_callback(value)

    # ---------- 对外入口 ----------
    def convert_files(
        self,
        paths: list[str | Path],
        output_dir: str | Path,
        method: str = "auto",
        subject: str = "",
        add_frontmatter: bool = True,
        postprocess: bool = True,
    ) -> dict:
        """批量转换。method: auto / cloud / local / ocr"""
        files = collect_files(paths)
        if not files:
            self.log("没有找到支持的文件。")
            return {"total": 0, "success": 0, "failed": 0, "results": []}

        out_root = Path(output_dir)
        out_root.mkdir(parents=True, exist_ok=True)

        results = []
        total = len(files)
        for idx, file in enumerate(files, 1):
            self.log(f"\n[{idx}/{total}] 开始处理: {file.name}")
            try:
                md_path = self.convert_file(
                    file,
                    out_root,
                    method=method,
                    subject=subject,
                    add_frontmatter=add_frontmatter,
                    postprocess=postprocess,
                )
                results.append({"file": str(file), "ok": True, "output": str(md_path)})
                self.log(f"  ✅ 完成: {md_path}")
            except Exception as e:
                results.append({"file": str(file), "ok": False, "error": str(e)})
                self.log(f"  ❌ 失败: {e}")
            self.progress(int(idx / total * 100))

        ok = sum(1 for r in results if r["ok"])
        self.log(f"\n=== 完成: 成功 {ok}/{total} ===")
        return {"total": total, "success": ok, "failed": total - ok, "results": results}

    def convert_file(
        self,
        file: str | Path,
        output_dir: str | Path,
        method: str = "auto",
        subject: str = "",
        add_frontmatter: bool = True,
        postprocess: bool = True,
    ) -> Path:
        file = Path(file)
        out_root = Path(output_dir)
        out_root.mkdir(parents=True, exist_ok=True)

        method = (method or "auto").lower()
        if method == "auto":
            if self._has_mineru():
                method = "cloud"  # 优先云 API，失败再本地
            else:
                method = "ocr"

        tmp_dir = Path(tempfile.mkdtemp(prefix="mineru_md_"))
        try:
            if method == "cloud":
                md_file = self._convert_cloud(file, tmp_dir)
            elif method == "local":
                md_file = self._convert_local(file, tmp_dir)
            elif method == "ocr":
                md_file = self._convert_ocr(file, tmp_dir)
            else:
                raise ValueError(f"未知转换方式: {method}")

            if md_file is None or not Path(md_file).exists():
                raise RuntimeError("转换后未找到 Markdown 输出")

            # 每个源文件输出到一个独立文件夹：out_root/<源文件名>/
            file_out_dir = out_root / file.stem
            file_out_dir.mkdir(parents=True, exist_ok=True)
            final_md = file_out_dir / f"{file.stem}.md"
            shutil.copy2(md_file, final_md)

            # 如果有 images 目录，一起放到该输出文件夹内
            src_images = Path(md_file).parent / "images"
            if src_images.is_dir():
                dst_images = file_out_dir / "images"
                if dst_images.exists():
                    shutil.rmtree(dst_images)
                shutil.copytree(src_images, dst_images)

            if add_frontmatter:
                self._add_frontmatter(
                    final_md,
                    source_name=file.name,
                    subject=subject or file.stem,
                    parser="mineru" if method in ("cloud", "local") else "ocr",
                )

            if postprocess:
                self._postprocess(final_md)

            return final_md
        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    # ---------- 云 API ----------
    def _has_mineru(self) -> bool:
        return bool(self.config.get("mineru_api_token")) or shutil.which(self.config.get("mineru_command", "mineru"))

    def _convert_cloud(self, file: Path, tmp_dir: Path) -> Path:
        token = self.config.get("mineru_api_token", "")
        if not token:
            self.log("  未配置 MinerU API Token，尝试本地 MinerU...")
            return self._convert_local(file, tmp_dir)
        return self._cloud_api_generic(file, tmp_dir, token)

    def _cloud_api_generic(self, file: Path, out_dir: Path, token: str) -> Path:
        import io
        import zipfile

        import requests

        api = self.config.get("mineru_api_url", "https://mineru.net/api/v4")
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

        model_version = self.config.get("mineru_model_version", "vlm")
        self.log("  上传到 MinerU 云 API ...")
        r = requests.post(
            f"{api}/file-urls/batch",
            headers=headers,
            json={"files": [{"name": file.name}], "model_version": model_version},
            timeout=30,
        )
        if r.status_code != 200:
            raise RuntimeError(f"获取上传地址失败: {r.status_code} {r.text[:200]}")

        data = r.json()["data"]
        upload_url = data["file_urls"][0]
        batch_id = data["batch_id"]

        with open(file, "rb") as f:
            up = requests.put(upload_url, data=f, timeout=300)
        if up.status_code not in (200, 201, 204):
            raise RuntimeError(f"上传失败: {up.status_code}")

        self.log("  等待 MinerU 处理 ...")
        for i in range(180):
            time.sleep(5)
            r = requests.get(
                f"{api}/extract-results/batch/{batch_id}",
                headers=headers,
                timeout=30,
            )
            if r.status_code != 200:
                continue
            res = r.json().get("data", {})
            extracts = res.get("extract_result", [])
            if not extracts:
                continue
            extract = extracts[0]
            state = extract.get("state", "?")
            if state == "done":
                zurl = extract.get("full_zip_url", "")
                if not zurl:
                    raise RuntimeError("MinerU 完成但缺少下载地址")
                zr = requests.get(zurl, timeout=300)
                z = zipfile.ZipFile(io.BytesIO(zr.content))
                z.extractall(out_dir)
                md_files = [n for n in z.namelist() if n.endswith(".md")]
                if not md_files:
                    raise RuntimeError("MinerU 返回内容中没有 Markdown")
                md_path = out_dir / md_files[0]
                # 有些压缩包内 MD 在子目录，转成 out_dir/merged.md
                if md_path.parent != out_dir:
                    merged = out_dir / "merged.md"
                    shutil.copy2(md_path, merged)
                    md_path = merged
                self.log(f"  云 API 完成: {len(md_files)} 个 md")
                return md_path
            elif state == "failed":
                raise RuntimeError(f"MinerU 处理失败: {extract.get('err_msg', 'unknown')}")
            if i % 12 == 0:
                self.log(f"  状态: {state} ({(i+1)*5}s)")

        raise RuntimeError("等待 MinerU 云 API 超时")

    # ---------- 本地 MinerU ----------
    def _convert_local(self, file: Path, tmp_dir: Path) -> Path:
        cmd = self.config.get("mineru_command", "mineru")
        backend = self.config.get("mineru_backend", "pipeline")
        lang = self.config.get("mineru_lang", "ch")

        if not shutil.which(cmd):
            raise RuntimeError(f"未找到本地 mineru 命令: {cmd}")

        self.log(f"  本地 MinerU: {cmd} -b {backend} -l {lang}")
        subprocess.run(
            [cmd, "-p", str(file), "-o", str(tmp_dir), "-b", backend, "-l", lang],
            check=True,
            timeout=1800,
        )

        md_files = list(Path(tmp_dir).rglob("*.md"))
        if not md_files:
            raise RuntimeError("本地 MinerU 未生成 Markdown")
        # 选最大的 md，通常是主文件
        return max(md_files, key=lambda p: p.stat().st_size)

    # ---------- OCR 兜底 ----------
    def _convert_ocr(self, file: Path, tmp_dir: Path) -> Path:
        tesseract = self.config.get("tesseract_path", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
        if not os.path.exists(tesseract):
            # 尝试 PATH 中的 tesseract
            tesseract = shutil.which("tesseract") or tesseract
        if not os.path.exists(tesseract):
            raise RuntimeError(f"未找到 Tesseract: {tesseract}")

        md_parts = []
        ext = file.suffix.lower()

        if ext == ".pdf":
            pages = self._pdf_to_pngs(file, tmp_dir)
            if not pages:
                raise RuntimeError("pdftocairo 未能生成图片")
            for idx, png in enumerate(pages, 1):
                text = self._ocr_image(png, tesseract)
                md_parts.append(f"## 第 {idx} 页\n\n{text.strip()}\n")
        elif ext in {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}:
            text = self._ocr_image(file, tesseract)
            md_parts.append(text.strip())
        else:
            raise RuntimeError(f"OCR 兜底暂不支持该格式: {ext}")

        md_path = tmp_dir / "ocr_output.md"
        md_path.write_text("\n\n".join(md_parts), encoding="utf-8")
        return md_path

    def _pdf_to_pngs(self, pdf_path: Path, tmp_dir: Path) -> list[Path]:
        cmd = self.config.get("pdftocairo_command", "pdftocairo")
        pattern = tmp_dir / "page"
        subprocess.run(
            [cmd, "-png", "-r", "300", str(pdf_path), str(pattern)],
            check=True,
            timeout=600,
        )
        return sorted(tmp_dir.glob("page-*.png"))

    def _ocr_image(self, image: Path, tesseract: str) -> str:
        result = subprocess.run(
            [tesseract, str(image), "-", "-l", "chi_sim+eng", "--psm", "4"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
        return result.stdout

    # ---------- frontmatter / 后处理 ----------
    def _add_frontmatter(self, md_path: Path, source_name: str, subject: str, parser: str):
        content = md_path.read_text(encoding="utf-8", errors="replace")
        if content.lstrip().startswith("---"):
            return
        status = "mineru解析" if parser in ("mineru", "mineru-vlm") else "OCR转换（待校对）"
        fm = f"""---
raw_title: {Path(source_name).stem}
subject: {subject}
source: {source_name}
status: {status}
parser: {parser}
---

"""
        md_path.write_text(fm + content, encoding="utf-8")

    def _postprocess(self, md_path: Path):
        text = md_path.read_text(encoding="utf-8", errors="replace")
        text = fix_cjk_spaces(text)
        text = fix_damaged_latex(text)
        text = fix_math_unicode(text)
        md_path.write_text(text, encoding="utf-8")

        # 检测残留
        unicode_left = re.findall(r"[\U0001D400-\U0001D7FF]", text)
        if unicode_left:
            self.log(f"  ⚠️ 仍有 {len(unicode_left)} 处 Unicode 数学斜体残留")
        if "$???$" in text:
            self.log("  ⚠️ 存在 $???$，可能需要人工检查")

    @staticmethod
    def _rewrite_image_refs(md_path: Path, old_prefix: str, new_prefix: str):
        content = md_path.read_text(encoding="utf-8", errors="replace")
        content = content.replace(f"]({old_prefix}/", f"]({new_prefix}/")
        content = content.replace(f"]({old_prefix}/", f"]({new_prefix}/")
        content = content.replace(f'"{old_prefix}/', f'"{new_prefix}/')
        md_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    # 简单命令行测试
    if len(sys.argv) < 3:
        print(__doc__)
        print("用法: python converter.py <输入文件或目录> <输出目录> [method] [subject]")
        sys.exit(1)
    conv = Converter()
    result = conv.convert_files(
        [sys.argv[1]],
        sys.argv[2],
        method=sys.argv[3] if len(sys.argv) > 3 else "auto",
        subject=sys.argv[4] if len(sys.argv) > 4 else "",
    )
    print(result)
