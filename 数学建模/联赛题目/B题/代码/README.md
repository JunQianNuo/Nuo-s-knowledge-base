# CLB_B Python 工程

本目录是可独立移动和分享的 Python 工程根目录。共享的数据模型、加载、可行性、指标和验证代码位于 `common/`；各题源码、测试、输出、日志和缓存分别归入 `q1/`、`q2/`、`q3/`。

## 目录结构

- `common/`：三问共享模块
- `q1/`：Q1 求解器及其算法、I/O、测试和运行文件
- `q2/`、`q3/`：后续问题的包与预留运行目录
- `tests/`：仅测试 common 层
- `scripts/`：工程审计和环境信息脚本；`scripts/local/` 仅存本机工具
- `.cache/`：pytest 与 Ruff 缓存

## 环境与检查

进入本目录后执行：

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m ruff check .
```

项目不绑定 Conda、WSL 或任何特定解释器路径。在 VS Code 中使用 `Python: Select Interpreter` 选择自己的环境即可。

## 数据

程序按以下顺序解析数据目录：

1. `--data-dir PATH`
2. 环境变量 `CLB_B_DATA_DIR`
3. `代码/data/`
4. 本目录父目录下包含全部四个官方 CSV 的附件目录

所需文件为 `distances.csv`、`peopleQ1.csv`、`peopleQ2.csv`、`peopleQ3.csv`。若无法发现，程序会提示使用 `--data-dir`；若发现内容不同的同名文件，程序会报错。

## 运行

Q1 快速检查：

```bash
python -m q1 --quick --workers 8
```

Q1 正式运行：

```bash
python -m q1 --workers 8
```

指定外部数据或输出目录：

```bash
python -m q1 --data-dir "PATH"
python -m q1 --output-dir "PATH"
```

小实例双模型交叉验证与参数敏感性实验：

```bash
python -m q1.run_q1_toy
python -m q1.run_q1_experiments            # 只打印实验矩阵
python -m q1.run_q1_experiments --execute  # 真正执行
```

Q2、Q3 尚未实现；`python -m q2` 与 `python -m q3` 只会给出明确状态提示。

## 当前状态

- Q1：候选簇枚举 + 精确航线 DP + 架次—人员流整数规划，已完成人员回填与独立
  CSV 复核；算法说明见 `q1/Q1算法分析.md`
- Q2：尚未实现求解器
- Q3：尚未实现求解器
