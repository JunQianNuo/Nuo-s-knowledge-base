# Q1 单向出海运载计划

## 目录

- `algorithms/`
  - `route_dp.py`：给定 (机场, 机型, 设施集合) 的**受限加油候选集内**最短用时航线精确求解
    （排列枚举 + 顺序内加油插入的 Dijkstra 标号法）
  - `clusters.py`：候选簇枚举、候选航线列构造、机型 Pareto 剪枝、候选池筛选、
    解引导的大邻域扩池
  - `greedy.py`：贪心初始可行解（主问题的启动提示）
  - `flow_master.py`：架次—人员流整数规划主问题（CP-SAT，词典序五级目标）
  - `flight_builder.py`：(y, z) → 具体架次副本，以及不劣化的局部改进
- `io/`：官方 CSV 写出与独立 CSV 复核
- `tests/`：Q1 专属测试（含与暴力枚举、与集合划分模型的交叉验证）
- `outputs/`：正式结果、`experiments/`、`archive/`
- `Q1算法分析.md`：算法逻辑与复杂度分析

从 `代码/` 运行：

```bash
python -m q1 --quick --workers 8   # 冒烟运行，约 3 分钟
python -m q1 --workers 8           # 正式运行
python -m q1.run_q1_toy            # 小实例双模型交叉验证
```

可用 `--efficiency-slack`、`--lns-rounds`、`--primary-seconds`、
`--secondary-seconds`、`--refuel-keep` 覆盖默认参数，用 `--data-dir` /
`--output-dir` 指定路径。

## 候选池敏感性

`refuel_keep=4/8` 实验复用同一 seed 和 solver 配置，所有单次结果写入独立目录并
由 Q1 validator 检查，不覆盖正式输出：

```bash
python -m q1.run_sensitivity --quick
python -m q1.run_sensitivity --quick --execute --workers 8 --seed 20260815
```

汇总文件为 `q1/outputs/sensitivity/sensitivity_q1.csv`。不加 `--execute` 只打印
实验矩阵。当前未加入 cluster neighbourhood small/large，以避免把两个因素混在
同一轮 refuel 候选敏感性中。

seed `20260815`、8 workers 的 quick 实测均通过 validator：`refuel_keep=4` 的
候选池为 1603、T_air=14837；`refuel_keep=8` 的候选池为 1622、T_air=14908。
两次均是有限预算下的可行结果，不能仅凭该次运行断言 keep=4 恒优于 keep=8。

## 输出

| 文件 | 内容 |
| --- | --- |
| `q1-routes.csv` | 官方模板：架次停靠序列与加油标记 |
| `q1-assignments.csv` | 官方模板：每名人员的架次与上下机停靠序号 |
| `q1-flight-plan.csv` | 架次级明细（机场、机型、载客构成），便于人工抽查 |
| `q1-history.csv` | 各阶段五项指标、候选池规模、LP 下界与求解器界 |
| `q1-summary.json` | 汇总指标、下界、间隙与验证结论 |

## 认证范围

主问题在**有限候选航线池**上求解，报告的最优性与间隙都相对于该池的 LP 下界，
不声称是原问题全局最优。所有结果 CSV 均由 `io/csv_validator.py` 从文件重新
读入、独立重算路线闭环、着陆次数、加油合法性、动态容量、油量与五项指标。
