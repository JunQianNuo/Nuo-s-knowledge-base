---
title: skill-creator
type: Skill
status: 已安装
date: 2026-06-12
---

# skill-creator

Skill 创建与迭代优化引擎。

## 完整功能

### 核心循环

设计 → 草稿 → 测试 → 评估 → 改进 → 重复

### 创建流程

1. **捕获意图**：Skill 做什么？何时触发？输出格式？需要测试吗？
2. **访谈与研究**：问清边界情况、输入输出、示例文件、成功标准
3. **编写 SKILL.md**：YAML frontmatter（name + description）+ Markdown 正文

### 三层渐进加载

1. **Metadata**（name+description）— 始终在上下文（~100 词）
2. **SKILL.md body** — 触发时加载（<500 行理想）
3. **Bundled resources** — 按需加载（scripts/references/assets）

### 目录结构

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - 可执行代码
    ├── references/ - 按需加载文档
    └── assets/     - 模板/图标/字体
```

### 测试与评估

- 2-3 个真实测试用例，保存到 `evals/evals.json`
- 并行运行 with-skill + baseline（无 skill 或旧版）
- 定量断言 + 定性评审
- `eval-viewer/generate_review.py` 生成浏览器评审界面

### 改进原则

- 从反馈泛化，不针对特定案例过拟合
- 保持 prompt 精简，删除无效内容
- 解释「为什么」，而非强制「必须」
- 发现跨测试重复操作 → 打包成 script

### Description 优化

20 个触发评估查询（应触发 + 不应触发 mix）→ 60% 训练 / 40% 测试 → 最多 5 轮迭代优化 description 触发准确率

### 最终打包

`python -m scripts.package_skill <path>` → 生成 `.skill` 文件
