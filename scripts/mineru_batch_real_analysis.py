"""
Batch convert 实变函数 PDFs to MD via MinerU cloud API.
Free tier: 2000 pages/day. Total: ~303 pages across 25 PDFs.
"""
import requests, os, time, zipfile, io, glob, shutil, re, sys

# Fix GBK encoding in Git Bash terminal
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

os.environ['NO_PROXY'] = '*'

TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiIzNjgwMDY4MSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc4MTI5MzkxMCwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTczNDY3NzcxNTAiLCJvcGVuSWQiOm51bGwsInV1aWQiOiIyMjc3ZjM4NS01ZDkyLTRhMTYtODY1NC1lYzAzNjA3MTY3MzciLCJlbWFpbCI6IiIsImV4cCI6MTc4OTA2OTkxMH0.-oOsgQxugdghPbZHG-6wYtVfPyDZSMw5NKiXv-dIJXag0Ofo4TZtKLNHRX4tsXd0K_rS9suaVEwY7bKbE2bP2g"
API = "https://mineru.net/api/v4"
PROXIES = {'http': None, 'https': None}
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

PDF_DIR = r"D:\知识库\课程\实变函数\课件\PDF"
MD_DIR = r"D:\知识库\课程\实变函数\课件\MD"
IMG_DIR = r"D:\知识库\RA-images"  # All images go here, referenced as ![[RA-images/hash.jpg]]

os.makedirs(MD_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

pdf_files = sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf")))
print(f"Found {len(pdf_files)} PDF files")

CHAPTER_MAP = {
    "RA-01": "第1章 集合论基础与课程简介",
    "RA-02": "第2章 集合的运算与映射",
    "2023-RA-03": "第3章 映射与函数",
    "2023-RA-03-a": "第3章补充 映射的性质",
    "2023-RA-04-05": "第4-5章 集合的势与可数集",
    "2023-RA-06": "第6章 开集与闭集",
    "2023-RA-07": "第7章 紧集与完备集",
    "2023-RA-08": "第8章 集合的代数与σ-代数",
    "2023-RA-09": "第9章 自然数到实数的构造",
    "2023-RA-09-I": "第9章补充 实数构造详述",
    "2023-RA-11": "第11章 Lebesgue测度引言",
    "2023-RA-12": "第12章 外测度",
    "2023-RA-13": "第13章 可测集与Lebesgue测度",
    "2023-RA-14": "第14章 测度的性质",
    "2023-RA-15": "第15章 不可测集",
    "2023-RA-16": "第16章 可测函数",
    "2023-RA-17": "第17章 可测函数的性质",
    "2023-RA-18": "第18章 简单函数与逼近",
    "2023-RA-19": "第19章 几乎处处收敛",
    "2023-RA-20": "第20章 依测度收敛",
    "2023-RA-21": "第21章 Egorov定理与Lusin定理",
    "2023-RA-22": "第22章 Lebesgue积分定义",
    "2023-RA-23": "第23章 Lebesgue积分的性质",
    "2023-RA-24": "第24章 控制收敛定理",
    "2023-RA-25": "第25章 重积分与Fubini定理",
}


def convert_pdf(pdf_path):
    """Convert a single PDF via MinerU API. Returns (True, md_content, img_list) or (False,)."""
    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    print(f"\n{'='*60}")
    print(f"[{basename}] Starting...")

    # Step 1: Get upload URL
    r = requests.post(f"{API}/file-urls/batch", headers=HEADERS,
        json={"files": [{"name": f"{basename}.pdf"}], "model_version": "vlm"},
        timeout=30, proxies=PROXIES)

    if r.status_code != 200:
        print(f"  ERROR getting upload URL: {r.status_code} {r.text[:200]}")
        return (False,)

    data = r.json().get("data", {})
    upload_url = data.get("file_urls", [None])[0]
    batch_id = data.get("batch_id")
    if not upload_url or not batch_id:
        print(f"  ERROR: No upload URL or batch_id")
        return (False,)

    # Step 2: Upload PDF
    with open(pdf_path, "rb") as f:
        r = requests.put(upload_url, data=f, timeout=120, proxies=PROXIES)
    if r.status_code != 200:
        print(f"  ERROR uploading: {r.status_code}")
        return (False,)

    # Step 3: Poll until done
    for i in range(180):
        time.sleep(5)
        r = requests.get(f"{API}/extract-results/batch/{batch_id}",
                        headers=HEADERS, timeout=30, proxies=PROXIES)
        if r.status_code != 200:
            continue

        res = r.json().get("data", {})
        extracts = res.get("extract_result", [])
        if not extracts:
            if i % 12 == 0:
                print(f"  Waiting for extract_result... ({(i+1)*5}s)")
            continue

        extract = extracts[0]
        state = extract.get("state", "?")

        if state == "done":
            zurl = extract.get("full_zip_url", "")
            if not zurl:
                print(f"  ERROR: done but no zip URL")
                return (False,)

            r2 = requests.get(zurl, timeout=120, proxies=PROXIES)
            z = zipfile.ZipFile(io.BytesIO(r2.content))

            # Find MD content
            md_files = [n for n in z.namelist() if n.endswith('.md')]
            if not md_files:
                print(f"  ERROR: no .md file in output")
                return (False,)

            md_content = z.read(md_files[0]).decode("utf-8", errors="replace")

            # Copy images to shared RA-images folder, collect mapping
            img_map = {}  # old_name -> new_name (hash prefix + basename)
            img_count = 0
            for n in z.namelist():
                if n.startswith("images/") and not n.endswith('/'):
                    orig_name = os.path.basename(n)
                    # Use basename prefix to avoid collisions between PDFs
                    new_name = f"{basename}_{orig_name}"
                    dest = os.path.join(IMG_DIR, new_name)
                    if not os.path.exists(dest):
                        with open(dest, "wb") as f:
                            f.write(z.read(n))
                    img_map[orig_name] = new_name
                    img_count += 1

            print(f"  Done! {len(md_content)} chars, {img_count} images")
            return (True, md_content, img_map)

        elif state == "failed":
            print(f"  FAILED: {extract.get('err_msg', 'unknown')}")
            return (False,)

        if i % 12 == 0:
            print(f"  Polling... state={state} ({(i+1)*5}s)")

    print(f"  TIMEOUT")
    return (False,)


def fix_image_refs(md_content, img_map, basename):
    """Replace MinerU image refs with Obsidian wiki-links."""
    def replace_img(match):
        old_path = match.group(0)
        # Extract filename from images/xxx.jpg
        m = re.search(r'images/([^)\s]+)', old_path)
        if not m:
            return old_path
        fname = m.group(1)
        new_name = img_map.get(fname)
        if new_name:
            return f"![[RA-images/{new_name}]]"
        return old_path

    md_content = re.sub(r'!\[.*?\]\(images/[^)]+\)', replace_img, md_content)
    return md_content


def add_frontmatter(md_content, basename):
    """Add proper YAML frontmatter."""
    title = CHAPTER_MAP.get(basename, basename)
    return f"""---
title: {title}
subject: 实变函数
source: {basename}.pdf
status: mineru解析
parser: mineru-vlm
topics:
  - 实变函数
---
{md_content}"""


def main():
    results = []
    for idx, pdf_path in enumerate(pdf_files):
        basename = os.path.splitext(os.path.basename(pdf_path))[0]
        out_md = os.path.join(MD_DIR, f"{basename}.md")

        # Backup old xparse version if exists (always convert, never skip)
        if os.path.exists(out_md):
            old_backup = out_md.replace('.md', '.xparse_backup.md')
            shutil.copy2(out_md, old_backup)
            print(f"\n[{basename}] Backed up old xparse version")
        else:
            print()

        print(f"[{idx+1}/{len(pdf_files)}] {basename}.pdf")

        result = convert_pdf(pdf_path)
        if not result[0]:
            print(f"  ❌ FAILED")
            results.append((basename, False))
            continue

        _, md_content, img_map = result

        # Fix image references
        md_content = fix_image_refs(md_content, img_map, basename)

        # Add frontmatter
        md_content = add_frontmatter(md_content, basename)

        # Write output (overwrite old xparse version)
        with open(out_md, "w", encoding="utf-8") as f:
            f.write(md_content)

        print(f"  ✓ Saved ({len(md_content)} chars, {len(img_map)} images)")
        results.append((basename, True))
        time.sleep(2)  # Be nice to the API

    # Summary
    success = sum(1 for _, ok in results if ok)
    failed = sum(1 for _, ok in results if not ok)
    print(f"\n{'='*60}")
    print(f"SUMMARY: {success} success, {failed} failed, {len(results)} total")
    print(f"MD files: {MD_DIR}")
    print(f"Images: {IMG_DIR}")

if __name__ == "__main__":
    main()
