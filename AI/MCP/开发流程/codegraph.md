---
title: CodeGraph
type: MCP
status: 已安装
source:
  - npm: "@colbymchenry/codegraph"
  - github: "https://github.com/colbymchenry/codegraph"
  - url: "https://getcodegraph.com"
date: 2026-06-12
---

# CodeGraph

预索引的语义代码知识图谱 MCP。将代码库解析为符号关系图（调用链、路由映射、跨语言桥接），让 AI Agent 直接查图而非反复 grep/glob/Read。

## 原理

```
传统方式：Agent subagent → grep → glob → Read × N → 拼凑理解
CodeGraph：Tree-sitter 解析 → SQLite 符号图 → 1 次 MCP 工具调用 → 完整答案
```

- **省 58% 工具调用** · **省 16% 成本** · **快 22%**（7 个真实代码库基准测试）
- 20+ 语言 Tree-sitter 解析
- 100% 本地，SQLite 存储，无数据外泄
- 操作系统原生文件监听器自动增量同步

## 安装

```bash
npm install -g @colbymchenry/codegraph

# 配置 Claude Code
codegraph install

# 初始化项目索引
cd your-project
codegraph init -i
```

已安装版本：`0.9.9`

## MCP 工具（8 个）

| 工具 | 用途 | 例子 |
|------|------|------|
| `codegraph_explore` | 一次查询返回入口点 + 相关符号 + 代码片段 | "认证模块怎么实现的？" |
| `codegraph_search` | FTS5 全文搜索整个代码库 | 搜函数名/类名/字面量 |
| `codegraph_callers` | 谁调用了这个符号 | 改签名前看所有调用方 |
| `codegraph_callees` | 这个符号调用了谁 | 追踪执行路径 |
| `codegraph_impact` | 改动影响半径（callers + callees + 路由） | PR 评审：改这个影响哪些功能 |
| `codegraph_node` | 单个符号的完整详情 | 查函数签名、类型、位置 |
| `codegraph_status` | 索引同步状态（待同步文件列表） | 确认图是否最新 |
| `codegraph_files` | 按路径查询文件级信息 | 列出模块下的所有符号 |

## 语言支持（20+）

TypeScript · JavaScript · Python · Go · Rust · Java · C# · PHP · Ruby · C · C++ · Objective-C · Swift · Kotlin · Scala · Dart · Lua · Luau · Svelte · Vue · Astro · Liquid · Pascal/Delphi

## 框架感知路由（17 个框架）

自动识别 web 框架路由文件，将 URL 模式链接到处理函数：

| 框架 | 识别模式 |
|------|----------|
| Django | `path()`/`re_path()`/`url()` in `urls.py` |
| Flask | `@app.route()` + blueprint routes |
| FastAPI | `@app.get()`/`@router.post()` 等 |
| Express | `app.get()`/`router.post()` + middleware chains |
| NestJS | `@Controller` + `@Get/@Post`/GraphQL `@Resolver`/`@MessagePattern` |
| Laravel | `Route::get()`/`Route::resource()` 等 |
| Drupal | `*.routing.yml` + hook 实现 |
| Rails | `get '/x', to: 'users#index'` |
| Spring | `@GetMapping`/`@PostMapping`/`@RequestMapping` |
| Play | `GET`/`POST` routes in `conf/routes` |
| Gin/chi/gorilla/mux | `r.GET()`/`router.HandleFunc()` |
| Axum/actix/Rocket | `.route("/x", get(handler))` |
| ASP.NET | `[HttpGet("/x")]` attributes |
| Vapor | `app.get("x", use: handler)` |
| React Router/SvelteKit | Route component nodes |
| Vue Router/Nuxt | `pages/` file-based routes + `server/api/` |
| Astro | `src/pages/` file-based routes |

## 跨语言 iOS / React Native 桥接

真实 iOS/RN 代码跨多种语言，静态解析在语言边界断裂。CodeGraph 连接它们：

| 边界 | 桥接方式 |
|------|----------|
| Swift → ObjC | `@objc` 自动桥接规则 + Cocoa 介词前缀 |
| ObjC → Swift | `@objc` 逆向候选验证 |
| RN legacy bridge | `RCT_EXPORT_METHOD` → JS `NativeModules.X.fn()` |
| RN TurboModules | `Native<X>.ts` 规格 → native 实现 |
| RN native → JS events | `sendEventWithName:` → `addListener('e', cb)` |
| Expo Modules | `Module { Name("X"); AsyncFunction("fn") { ... } }` |
| Fabric view components | Codegen spec → native 实现 |
| Legacy Paper view managers | `RCT_EXPORT_VIEW_PROPERTY` → JSX 组件 |

## 自动同步机制

三层保持索引最新：

| 层级 | 机制 |
|------|------|
| 文件监听 | 原生 FSEvents/inotify/ReadDirectoryChangesW，去抖 2s 后自动重新索引 |
| 过期标记 | 同步窗口期内，引用待更新文件的响应加 `⚠️` 横幅提示 agent 直接 `Read` |
| 连接补全 | MCP 重连时快速 `(size, mtime)` + hash 核对，吸收离线期间的编辑 |

手动触发同步：`codegraph sync`

## 基准测试（Opus 4.8，2026-06-02）

7 个真实代码库，每个 4 轮取中位数：

| 代码库 | 语言·规模 | 成本 | Token | 时间 | 工具调用 |
|--------|-----------|------|-------|------|----------|
| VS Code | TS·~10k 文件 | −18% | −64% | −11% | −81% |
| Excalidraw | TS·~640 | 持平 | −25% | −27% | −40% |
| Django | Python·~3k | −8% | −60% | −13% | −77% |
| Tokio | Rust·~790 | 持平 | −38% | −18% | −57% |
| OkHttp | Java·~645 | −25% | −54% | −31% | −50% |
| Gin | Go·~110 | −19% | −23% | −24% | −44% |
| Alamofire | Swift·~110 | −40% | −64% | −33% | −58% |

## 关联

- [[AI/Skill/开发流程/feature-dev/README|feature-dev]] — Phase 2 Codebase Exploration 的加速引擎
- [[AI/Skill/开发流程/superpowers/README|superpowers]] — 无直接关系（superpowers 方法论层，CodeGraph 基础设施层）
