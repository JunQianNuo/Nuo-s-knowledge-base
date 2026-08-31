from __future__ import annotations

import hashlib
import os
from pathlib import Path

DATA_FILENAMES = ("distances.csv", "peopleQ1.csv", "peopleQ2.csv", "peopleQ3.csv")

CODE_ROOT = Path(__file__).resolve().parents[1]
Q1_ROOT = CODE_ROOT / "q1"
Q1_OUTPUT_DIR = Q1_ROOT / "outputs"
Q1_LOG_DIR = Q1_ROOT / "logs"
Q1_CACHE_DIR = Q1_ROOT / "cache"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_data_dir(path: Path, source: str) -> Path:
    directory = path.expanduser().resolve()
    missing = [name for name in DATA_FILENAMES if not (directory / name).is_file()]
    if missing:
        raise FileNotFoundError(
            f"{source} 数据目录缺少文件: {', '.join(missing)}（目录: {directory}）"
        )
    return directory


def _auto_discover_data_dir() -> Path:
    local_data = CODE_ROOT / "data"
    if all((local_data / name).is_file() for name in DATA_FILENAMES):
        return local_data.resolve()

    matches: dict[str, list[Path]] = {
        name: sorted(
            path.resolve()
            for path in CODE_ROOT.parent.rglob(name)
            if CODE_ROOT not in path.resolve().parents
        )
        for name in DATA_FILENAMES
    }
    if any(not paths for paths in matches.values()):
        raise FileNotFoundError("未找到数据目录，请使用 --data-dir 指定。")

    for filename, paths in matches.items():
        hashes = {_sha256(path) for path in paths}
        if len(hashes) > 1:
            listed = "\n".join(str(path) for path in paths)
            raise RuntimeError(f"发现内容不同的同名数据文件 {filename}:\n{listed}")

    directories_by_file = (set(path.parent for path in paths) for paths in matches.values())
    candidate_dirs = set.intersection(*directories_by_file)
    if not candidate_dirs:
        raise FileNotFoundError("未找到同时包含四个官方 CSV 的数据目录，请使用 --data-dir 指定。")
    return min(candidate_dirs, key=lambda path: (len(path.parts), str(path)))


def resolve_data_dir(data_dir: Path | str | None = None) -> Path:
    if data_dir is not None:
        return _validate_data_dir(Path(data_dir), "--data-dir")
    environment = os.environ.get("CLB_B_DATA_DIR")
    if environment:
        return _validate_data_dir(Path(environment), "CLB_B_DATA_DIR")
    return _auto_discover_data_dir()


def find_data_file(filename: str, data_dir: Path | str | None = None) -> Path:
    if filename not in DATA_FILENAMES:
        raise ValueError(f"未知数据文件: {filename}")
    return resolve_data_dir(data_dir) / filename


def data_paths(data_dir: Path | str | None = None) -> dict[str, Path]:
    directory = resolve_data_dir(data_dir)
    return {name: directory / name for name in DATA_FILENAMES}
