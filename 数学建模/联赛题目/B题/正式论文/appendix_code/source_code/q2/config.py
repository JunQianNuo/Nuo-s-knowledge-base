from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Q2Config:
    quick: bool = False
    seed: int = 20260815
    time_budget: float = 300.0
    workers: int = 8
    pair_limit: int = 500
    lns_rounds: int = 1
    primary_time_limit: float = 700.0
    secondary_time_limit: float = 300.0

    @classmethod
    def build(cls, *, quick: bool, seed: int, time_budget: Optional[float], workers: int):
        return cls(
            quick=quick,
            seed=seed,
            time_budget=time_budget if time_budget is not None else (60.0 if quick else 300.0),
            workers=workers,
            pair_limit=180 if quick else 700,
            lns_rounds=0 if quick else 2,
        )
