from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .paths import find_data_file


@dataclass(frozen=True)
class DistanceData:
    raw: pd.DataFrame
    distances: dict[tuple[str, str], float]
    locations: tuple[str, ...]

    def get(self, origin: str, destination: str) -> float:
        try:
            return self.distances[(origin, destination)]
        except KeyError as exc:
            raise KeyError(f"距离表缺少弧 {origin} -> {destination}") from exc


def _read_csv(
    filename: str, path: Path | None = None, data_dir: Path | None = None
) -> pd.DataFrame:
    source = path or find_data_file(filename, data_dir)
    try:
        return pd.read_csv(source, encoding="utf-8")
    except Exception as exc:
        raise ValueError(f"读取 {source} 失败: {exc}") from exc


def _require_columns(frame: pd.DataFrame, required: set[str], source: str) -> None:
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"{source} 缺少必要字段: {', '.join(missing)}")


def _validate_people(frame: pd.DataFrame, source: str, q3: bool = False) -> pd.DataFrame:
    required = {"person_id", "origin_id", "destination_id"}
    if q3:
        required |= {"earliest_pickup_time", "latest_arrival_time", "task_type"}
    _require_columns(frame, required, source)
    for column in required:
        if frame[column].isna().any() or frame[column].astype(str).str.strip().eq("").any():
            raise ValueError(f"{source} 字段 {column} 存在空值")
    duplicates = frame.loc[frame["person_id"].duplicated(), "person_id"].tolist()
    if duplicates:
        raise ValueError(f"{source} 存在重复 person_id: {duplicates[:5]}")
    result = frame.copy()
    if q3:
        for column in ("earliest_pickup_time", "latest_arrival_time"):
            try:
                result[column] = pd.to_datetime(result[column], errors="raise")
            except Exception as exc:
                raise ValueError(f"{source} 字段 {column} 含非法时间") from exc
        if (result["earliest_pickup_time"] > result["latest_arrival_time"]).any():
            raise ValueError(f"{source} 存在最早接人时刻晚于最晚到达时刻")
    return result


def load_distances(path: Path | None = None, data_dir: Path | None = None) -> DistanceData:
    frame = _read_csv("distances.csv", path, data_dir)
    _require_columns(frame, {"from_id"}, "distances.csv")
    if frame["from_id"].isna().any() or frame["from_id"].duplicated().any():
        raise ValueError("distances.csv 的 from_id 为空或重复")
    locations = tuple(str(value) for value in frame["from_id"])
    if set(frame.columns[1:]) != set(locations):
        raise ValueError("distances.csv 行地点与列地点集合不一致")
    numeric = frame.loc[:, list(locations)].apply(pd.to_numeric, errors="coerce")
    if numeric.isna().any().any() or (numeric < 0).any().any():
        raise ValueError("distances.csv 含缺失、非数值或负距离")
    distances = {
        (origin, destination): float(numeric.at[row_index, destination])
        for row_index, origin in enumerate(locations)
        for destination in locations
    }
    return DistanceData(frame.copy(), distances, locations)


def load_people_q1(path: Path | None = None, data_dir: Path | None = None) -> pd.DataFrame:
    return _validate_people(_read_csv("peopleQ1.csv", path, data_dir), "peopleQ1.csv")


def load_people_q2(path: Path | None = None, data_dir: Path | None = None) -> pd.DataFrame:
    return _validate_people(_read_csv("peopleQ2.csv", path, data_dir), "peopleQ2.csv")


def load_people_q3(path: Path | None = None, data_dir: Path | None = None) -> pd.DataFrame:
    return _validate_people(_read_csv("peopleQ3.csv", path, data_dir), "peopleQ3.csv", q3=True)
