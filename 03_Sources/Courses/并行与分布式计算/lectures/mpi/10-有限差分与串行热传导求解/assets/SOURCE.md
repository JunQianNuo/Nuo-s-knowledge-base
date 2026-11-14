# 图示来源与复现

核对日期：2026-11-01。所有图均为课程自绘。

- stencil.svg：三点旧层到一个新值的数据依赖，数学依据见讲义末尾 FNC 中心差分及 Demmel CS267 资料；不是进程通信图。
- solution-error：调用本例 heat_serial，N=20/40/80、t=10 s、请求 r=0.4；L=1 m、alpha=0.01 m²/s、两端 20 °C、初值 20+80 sin(pi x/L)。图为数值结果与解析误差。
- convergence：相同 CSV 的最大绝对误差；虚线是按首个误差缩放的 N^-2 趋势，不是另一组实验。
- stability：调用 stability_demo，N=20、模态 k=19、扰动 1e-6 K、40 步；r=0.4/0.6 对应不同物理步长，比较的是每步衰减/放大。

CSV 为实际 C 程序输出；results.json 保存摘要。复现：先编译例子，然后运行 `python3 generate_figures.py /absolute/path/to/10_heat_serial/build`。需要 Python 与 Matplotlib；绘图只使用英文标注，不依赖中文字体。SVG/PDF 为矢量，PNG 供预览；Beamer 的模板图使用原生 TikZ。

## 学生操作图：单组温度与误差

2026-11-09 新增 `csv-solution-N20.png/.pdf`，由本目录已有的真实 `solution-N20.csv` 经仓库统一脚本 `examples/mpi/plot_heat.py` 生成。上图为解析温度黑线与数值温度橙色节点，下图为逐点绝对误差；参数与原 `solution-error` 的 N=20 实验一致，最大误差为约 0.08500094 K。

学生在 `examples/mpi/10_heat_serial/build` 中复现：

```bash
./heat_serial 20 10 > solution-N20.csv
python3 ../../plot_heat.py solution-N20.csv -o solution-N20.png
```

改用 `.pdf` 扩展名即生成同内容矢量图。单文件给出终止时刻的空间分布；没有声称保存全部中间时间层。不同 N 单独绘制的误差面板会自动选取纵轴范围，比较时必须读取刻度与最大误差值。

概念依据：

- [FNC: Finite differences](https://fncbook.com/finitediffs/)
- [FNC: Absolute stability](https://fncbook.com/absstab-diffusion/)
- [Demmel: Heat equation discretization](https://people.eecs.berkeley.edu/~demmel/cs267/lecture17/lecture17.html)

- [Matplotlib: pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)：图片、矢量文件保存与格式选择；新增绘图资料核对日期为 2026-11-09。
