# 第九讲图示来源与复现

本目录图示均为课程自绘。结构图表达数学模型中的能量平衡；温度曲线和二维温度场由已知解析公式直接采样，**不是差分求解器的运行结果，也不是实测数据**。参数 L=1 m、α=0.01 m²/s、基准温度 20 °C、初始温差幅值 80 K 为课程假设，没有声称对应某种实际材料。资料核对日期：2026-10-27。

| 图 | 内容与数值依据 |
|---|---|
| `rod-energy-balance.svg` / `.pdf` | 均匀细杆侧面绝热、两端为恒温边界；热由高温向低温传递。小段中 q 采用 +x 正方向，q 可取正负；固定小段的积累速率等于流入功率减去流出功率。概念依据文献 1、2。 |
| `slope-vs-curvature.svg` / `.pdf` | 三个独立剖面分别为 T=100−80x、T=20+80sin(πx)、T=80−60sin(πx)，用于在 x=0.5 m 处比较斜率、曲率与局部温度变化的符号；无内部热源且 α>0。依据文献 1、3 的热方程。 |
| `heat-line-profiles.svg` / `.pdf` | T₁(x,t)=20+80exp[−α(π/L)²t]sin(πx/L)，绘制 t=0、5、10、20 s。解析模态依据文献 1、2；具体参数和采样数据为课程自编。 |
| `heat-plate-fields.svg` / `.pdf` | T₂(x,y,t)=20+80exp[−2α(π/L)²t]sin(πx/L)sin(πy/L)，绘制 t=0、10、20 s。三个面板共用 20–100 °C 色标，不随各图最大值自动缩放。二维热方程依据文献 2；本解可直接代入验证。 |

## 复现

`generate_figures.py` 使用 Python 3、NumPy 和 Matplotlib，并需要中文字体。脚本依次尝试 Hiragino Sans GB、Noto Sans CJK SC、Microsoft YaHei、SimHei、PingFang SC；若都不存在，会报错提示安装字体。Linux 可安装 Noto Sans CJK SC。执行后重新产生同名 SVG、PDF、PNG、两个 CSV 表和参数记录：

```bash
python generate_figures.py
```

该脚本只计算函数值，没有差分空间算子或时间推进循环。`heat-line-reference.csv` 保存 4 个时刻、每时刻 101 个空间采样点；`heat-plate-reference.csv` 保存 3 个时刻、每时刻 21×21 个空间采样点。采样密度用于画图和查看函数，不改变连续模型的解析温度。

`figure-parameters.json` 记录参数、衰减时间与两个中心温度。SVG 将文字转为矢量路径；PDF 使用 Matplotlib Type 3 矢量字形轮廓，保留清晰的文字形状，并避开 CFF/OpenType 字体嵌入的兼容性问题。PNG 是同一图的检查/预览版本。图和代码适用课程仓库的 MIT License；未复制外部图版。

## 学生操作图：从真实 CSV 绘图

2026-11-09 新增 `csv-line.png/.pdf` 与 `csv-plate.png/.pdf`。输入保存在 `plot-data/`：由课程 `09_heat_reference` 的 C 程序实际运行，默认参数 line / plate、t=0/10/20 s，未经改写。备课生成时在 macOS 上用系统 C 编译器编译现有 `main.c` 与 `heat_reference.c`；图由仓库统一 `examples/mpi/plot_heat.py` 读取这些 CSV 生成。它们仍是解析解参考程序的输出，不是有限差分结果。

学生从课程仓库根目录，按本讲构建后，在 `examples/mpi/09_heat_reference/build` 中复现：

```bash
for t in 0 10 20; do
  ./heat_reference line "$t" > "line-t${t}.csv"
  ./heat_reference plate "$t" > "plate-t${t}.csv"
done
python3 ../../plot_heat.py line-t0.csv line-t10.csv line-t20.csv -o rod.png
python3 ../../plot_heat.py plate-t0.csv plate-t10.csv plate-t20.csv -o plate.png
```

将 `-o` 后扩展名改为 `.pdf` 即生成同内容矢量图。课件一维图使用 PDF，二维图使用高分辨率 PNG，避免部分 PDF 渲染器在相邻色块间出现细线缝。二维图保留实际 11×11 采样点，`shading="nearest"` 按相邻节点中点显示色块，三个时刻固定 `vmin=20, vmax=100`；一维曲线保留实际 11 个节点。新增绘图资料核对日期：2026-11-09。

## 参考文献

1. Matthew J. Hancock，MIT 18.303，*The 1-D Heat Equation*，Fall 2006，§1.1–1.2（PDF 第 1–3 页）与 §2.3（第 7 页）。支持 Fourier 定律、控制体能量守恒、热扩散率、初边值条件和正弦模态。<https://www.ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/d11b374a85c3fde55ec971fe587f8a50_heateqni.pdf>
2. Stanford Math 220B，*2 Heat Equation*，§2.1–2.2（PDF 第 1–5 页）、§2.8（第 39–40 页）。支持任意维热方程、Dirichlet/Neumann 边界、正弦解及最大值原理。<https://web.stanford.edu/class/math220b/handouts/heateqn.pdf>
3. Bjorn Poonen，MIT 18.03，*Lecture Notes, Spring 2025*，§29.1 Remark 29.2（PDF 第 196 页）。支持曲率与局部升温/降温的解释。<https://math.mit.edu/~poonen/03/notes.pdf>

讲义中的数值算法总体思路另依据 Gilbert Strang（MIT 18.086，2006）§5.4 与 James Demmel（UC Berkeley CS267，1996-02-27 Lecture 13）的原课程材料，完整资料集中列于本讲末尾。

4. Matplotlib，[pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)：保存图片与矢量图。
5. Matplotlib，[pyplot.pcolormesh](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html)：颜色映射上下限与 nearest 节点着色。
