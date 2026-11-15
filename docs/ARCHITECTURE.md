# 仓库架构

本仓库位于 `D:/知识库`，是用于课程学习、资料归档和知识积累的 Obsidian 中文知识库，入口为 [[Home]]。

## 目录结构

```text
D:/知识库/
├── Home.md                 总入口
├── 00_Inbox/               待整理、缺失记录及待核实来源
├── 01_Knowledge/           可复用的概念、命题与方法，平铺存放
├── 02_Maps/                学科与主题导航（MOC）
├── 03_Sources/             来源资料与学习记录
│   ├── Books/              书籍资料
│   ├── Courses/            按课程保存笔记、课件、教材与作业
│   ├── Ideas/              自主想法
│   ├── Language/           语言学习
│   ├── Papers/             论文资料
│   ├── Readings/           阅读资料
│   ├── Reviews/            复习与综合整理
│   └── Web/                网页资料
├── 04_Assets/              独立或共享的附件与日程数据
│   ├── Documents/          文档附件
│   ├── Images/             图片附件
│   └── Schedule/           课表、作息与学期配置
├── 99_System/              知识库维护系统与任务规范
│   ├── knowledge/          知识管理程序、模板、Schema 与内部状态
│   ├── rules/              现行写作与任务处理规范
│   └── tools/              配套工具
├── docs/                   核心说明文档
├── scripts/                转换、检查、同步等处理脚本
└── 闪卡/                   按课程组织的闪卡资料
```

## 内容关系

- **来源资料**保存课堂、作业、阅读等原始记录与完整讲解。
- **知识原子**保存跨课程复用的概念、命题和方法，通过来源链接追溯依据。
- **主题导航**通过主题链接组织知识原子，可形成多层主题关系。
- **数据库视图**汇集主题、来源、课程、标签与待处理记录，入口由 Home 提供。

课程资料的配套 `images/`、`assets/` 与源文件保存在同一资料包内；`04_Assets` 存放独立或共享附件。

## 日程结构

`04_Assets/Schedule/` 中，`课表.base`、`作息表.base` 展示课程与作息记录；数据分别位于 `课程/<学期>/`、`作息/<学期>/`，各学期配置位于 `学期设置/<学期>.md`。学期名称形如 `2026-2027-第一学期`，根 `学期设置.md` 记录当前归档学期。

## 系统与说明文档

`99_System/rules/` 保存现行任务规范，`99_System/tools/` 保存配套工具；二者与 `knowledge/` 并列。规范入口为 [[99_System/rules/README]]。

`99_System/knowledge/` 保存知识管理程序、标准标签、测试与旧版兼容组件；其中 `v2/` 保存当前知识维护实现、模板、Schema、生成的数据库视图及内部状态。

`docs/` 包含 [[docs/AGENTS|AGENTS]]（执行规则）、[[docs/ARCHITECTURE|ARCHITECTURE]]（仓库架构）、[[docs/USAGE|USAGE]]（日常操作）和 [[docs/README|README]]（文档入口）。

`.obsidian/` 保存 Obsidian 配置；`.agents/`、`.claude/` 等隐藏目录保存 Agent 工具或本地运行配置。
