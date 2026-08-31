# Q2 求解程序

Q2 采用有限 `Physical Route Pool + Passenger Flow Master`。物理路线不预先固定人员数量，主问题用整数 `y_r` 和 `z_option` 决定架次副本及人员流，并对每个航段分别限制容量。

从 `代码/` 目录运行：

```bash
python -m q2.run_q2_toy
python -m q2 --quick --workers 8
python -m q2 --workers 8
```

支持 `--data-dir`、`--output-dir`、`--seed` 和 `--time-budget`。正式模式使用一个 overall deadline；有限路线池的结果只称 `pool-optimal` 或 `best validated feasible solution`。

输出位于 `q2/outputs/`，其中两个官方 CSV 严格保留模板字段；其他指标、认证和运行信息写入 `q2-summary.json`。
