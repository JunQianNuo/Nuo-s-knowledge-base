# Q3 七天具体飞机调度

Q3 使用有限 physical skeleton、临界时刻 TimedColumn、组级人员流和具体飞机
`AddNoOverlap` 排班，依次完成 mandatory 基准、temporary 接纳和五级词典序优化。
正式结果与 quick、敏感性实验目录相互隔离。

## 当前正式结果

- mandatory：3840/3840；
- temporary：160/160，满足率 100%；
- Stage A 基准：B0=35114（`formal_best_validated_feasible`）；
- Stage B：incumbent=160、bound=160、gap=0、OPTIMAL；
- Stage C：T_air=34033，T_pax=246808，fuel=273629.0，flights=204，
  utilization=0.4776725644；
- 官方 CSV independent validator：PASS，solver=delivery=validator。

Stage B 的人数认证范围是当前有限 TimedColumn 池及冻结 B0；整个 Q3 仍不能称为
原问题全局最优，因为 B0 本身是有限列池和有限预算下的最好已验证可行基准。

从 `代码/` 运行：

```bash
python -m q3 --stage-a --quick --workers 8
python -m q3 --stage-b --quick --workers 8
python -m q3 --stage-c --quick --workers 8
python -m q3 --workers 8
```

## 模型检验实验

```bash
# 默认分析 formal Stage B；加 --quick 分析 quick 产物
python -m q3.analyze_temporary_bottleneck

# 先查看矩阵，再显式执行；每组 A/B/C 都会独立验证
python -m q3.run_time_density_sensitivity --quick
python -m q3.run_time_density_sensitivity --quick --execute --workers 8
python -m q3.run_time_density_sensitivity --quick --collect-only
```

时间密度 `baseline` 使用区间的 earliest/midpoint/latest，`dense` 使用
earliest/25%/midpoint/75%/latest。实验写入 `q3/outputs/sensitivity/`，不会覆盖
quick、formal 或官方 CSV。所有实验保存 seed；默认 `20260815`。

Stage B summary 记录 `temporary_incumbent`、`temporary_best_bound`、
`temporary_gap` 和 `temporary_certified_optimal`。只有 CP-SAT 返回 `OPTIMAL`
才认证；否则即使 incumbent 合法也保持 false。当前 `q3-summary.json` 已记录
160/160、bound=160、gap=0 和 Stage B `OPTIMAL`。

未接纳原因是当前有限列池内的证据分类，不是原问题全空间中的反事实因果证明。
现存17人瓶颈文件是早期143人有限时间 incumbent 的诊断证据；后续正式搜索已达到
160/160，因此这17人并非结构性不可行。
完整实现与复杂度见 `Q3代码分析.md`，模型检验补充见 `Q3算法分析.md`。
