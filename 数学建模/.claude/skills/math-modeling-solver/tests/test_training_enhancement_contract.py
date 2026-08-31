"""Contract tests for the training-informed math-modeling-solver skill.

Runs with Python's standard library only. Exit 1 when one or more contractual
requirements are absent. This is intentionally a content/structure contract:
the artifact under test is an agent skill made of Markdown process rules.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
VAULT_ROOT = SKILL_ROOT.parents[2]
LEGACY_ROOT = VAULT_ROOT / ".agents" / "disabled-skills" / "math-modeling-solver-legacy"
EXPECTED_ORIGINAL_FILES = 61
EXPECTED_ORIGINAL_AGGREGATE_SHA256 = (
    "5f7575ebac492143bd5a67d445d79a007674f5fe542ffabdfe3408c84ed15c36"
)

failures: list[str] = []


def read(relative: str) -> str:
    path = SKILL_ROOT / relative
    if not path.is_file():
        failures.append(f"missing file: {relative}")
        return ""
    return path.read_text(encoding="utf-8-sig")


def require_terms(relative: str, terms: list[str]) -> None:
    text = read(relative)
    for term in terms:
        if term not in text:
            failures.append(f"{relative}: missing contract term: {term}")


def require_any(relative: str, alternatives: list[str], label: str) -> None:
    text = read(relative)
    if not any(item in text for item in alternatives):
        failures.append(f"{relative}: missing {label}: {alternatives}")


def aggregate_tree(root: Path) -> tuple[int, str]:
    files = sorted(path for path in root.rglob("*") if path.is_file())
    digest = hashlib.sha256()
    for path in files:
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return len(files), digest.hexdigest()


# 1. New focused references.
require_terms(
    "references/data-audit-and-baseline.md",
    ["数据结构指纹", "数据审计", "常识基线", "数学基准模型", "升级证据", "数据泄漏"],
)
require_terms(
    "references/algorithm-and-solver-engineering.md",
    [
        "通用算法契约",
        "算法专项检查",
        "求解器专项检查",
        "闭式公式",
        "机器学习",
        "随机优化",
        "蒙特卡洛",
        "ODE/PDE",
        "聚类",
        "最优间隙",
        "不可行诊断",
        "不适用",
    ],
)
require_terms(
    "references/competition-execution.md",
    ["团队协同", "滚动推进", "里程碑", "运行与复现清单", "随机种子", "AI 使用边界", "人工核验"],
)

# 2. Main skill routing and gates.
require_terms(
    "skill.md",
    [
        "全流程模式",
        "局部协助模式",
        "方案审查模式",
        "不强制创建完整目录",
        "数据审计报告",
        "模型阶梯",
        "通用算法契约",
        "算法专项检查",
        "求解器专项检查",
        "不得虚构求解状态或最优间隙",
        "Claim—Evidence",
        "AI 核验",
    ],
)
for reference in [
    "references/data-audit-and-baseline.md",
    "references/algorithm-and-solver-engineering.md",
    "references/competition-execution.md",
]:
    require_terms("skill.md", [reference])

# 3. Existing references receive focused enhancements.
require_terms(
    "references/problem-decomposition.md",
    ["观测单位", "重复测量", "截尾", "类别不平衡", "数据泄漏", "量纲"],
)
require_terms(
    "references/model-selection-matrix.md",
    ["常识基线", "数学基准模型", "升级证据", "复杂度代价", "回退"],
)
require_terms(
    "references/cookbook-optimization.md",
    ["求解状态", "incumbent", "bound", "gap", "不可行诊断", "冲突约束", "无界", "不得虚构"],
)
require_terms(
    "references/validation-planning.md",
    ["最低检验集合", "关键类别", "扰动稳定性", "权重敏感性", "不确定性"],
)
require_terms(
    "references/figure-planning.md",
    ["处理前后", "基准模型", "升级模型", "残差", "不确定性", "最优间隙", "现实方案"],
)
require_terms(
    "references/result-analysis.md",
    ["基准结果", "随机算法", "多次独立运行", "求解状态", "最优间隙", "预测—决策", "现实方案"],
)
require_terms(
    "references/paper-bridge.md",
    ["Claim—Evidence", "题意依据", "代码入口", "检验编号", "变量、单位和索引", "PAPER_READY"],
)

# 4. Behavior-level textual guarantees from B1-B14.
require_any("skill.md", ["时间顺序划分", "按时间验证", "时序验证"], "time-series leakage guard")
require_any("skill.md", ["总体准确率", "关键类别"], "class-imbalance guard")
require_any("skill.md", ["冲突约束", "最小松弛"], "infeasibility diagnosis")
require_any("skill.md", ["incumbent", "当前可行解"], "timeout incumbent reporting")
require_any("skill.md", ["回源核验", "权威来源"], "AI/source verification")
require_any("skill.md", ["变量、参数和约束字典", "变量、参数与约束字典"], "shared dictionary")

# 5. Relative Markdown references from the main skill must resolve.
main = read("skill.md")
for target in re.findall(r"`((?:\.\./)+(?:[^`]+/)*references/[^`]+?\.md|references/[^`]+?\.md)`", main):
    if not (SKILL_ROOT / target).resolve().is_file():
        failures.append(f"skill.md: broken relative reference: {target}")

# 6. No incomplete placeholders in files in implementation scope.
scope = [
    "skill.md",
    "references/data-audit-and-baseline.md",
    "references/algorithm-and-solver-engineering.md",
    "references/competition-execution.md",
    "references/problem-decomposition.md",
    "references/model-selection-matrix.md",
    "references/cookbook-optimization.md",
    "references/validation-planning.md",
    "references/figure-planning.md",
    "references/result-analysis.md",
    "references/paper-bridge.md",
]
for relative in scope:
    text = read(relative)
    for pattern in [r"\bTBD\b", r"\bTODO\b", r"稍后补充"]:
        if re.search(pattern, text, re.IGNORECASE):
            failures.append(f"{relative}: incomplete placeholder matches {pattern}")

# 7. Disabled legacy skill isolation.
count, aggregate = aggregate_tree(LEGACY_ROOT)
if count != EXPECTED_ORIGINAL_FILES:
    failures.append(f"legacy file count changed: expected {EXPECTED_ORIGINAL_FILES}, got {count}")
if aggregate != EXPECTED_ORIGINAL_AGGREGATE_SHA256:
    failures.append(
        "legacy aggregate hash changed: "
        f"expected {EXPECTED_ORIGINAL_AGGREGATE_SHA256}, got {aggregate}"
    )

if failures:
    print(f"FAIL: {len(failures)} contract violation(s)")
    for item in failures:
        print(f"- {item}")
    sys.exit(1)

print("PASS: training enhancement contract satisfied")
print(f"Legacy isolation: {count} files, aggregate SHA-256 {aggregate}")
