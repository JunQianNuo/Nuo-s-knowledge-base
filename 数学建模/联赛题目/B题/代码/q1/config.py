from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Q1AlgorithmConfig:
    """Q1 求解参数。

    - neighbourhood[k] = w：枚举规模为 k 的候选簇时，只在种子设施的前 w 个最近
      邻中取其余成员；
    - efficiency_slack / columns_per_group：候选池筛选强度。实验表明"较小但更
      锐利的池 + 多轮解引导扩池"显著优于"一次性大池"，因为主问题的搜索代价随
      列数快速上升；
    - 三个时间上限分别用于主目标首解、每轮 LNS 重解、以及词典序次级优化。
    """

    neighbourhood: dict[int, int] = field(
        default_factory=lambda: {2: 14, 3: 9, 4: 7, 5: 6}
    )
    efficiency_slack: float = 0.16
    columns_per_group: int = 8
    lns_rounds: int = 4
    lns_swap_width: int = 6
    primary_time_limit_seconds: float = 240.0
    lns_time_limit_seconds: float = 240.0
    secondary_time_limit_seconds: float = 150.0
    dinkelbach_max_iterations: int = 12
    refuel_keep: int = 4
    max_feedback_rounds: int = 3
    seed: int = 20260815


QUICK_CONFIG = Q1AlgorithmConfig(
    neighbourhood={2: 8, 3: 6, 4: 5, 5: 5},
    efficiency_slack=0.15,
    columns_per_group=6,
    lns_rounds=1,
    primary_time_limit_seconds=60.0,
    lns_time_limit_seconds=45.0,
    secondary_time_limit_seconds=10.0,
    max_feedback_rounds=1,
)
