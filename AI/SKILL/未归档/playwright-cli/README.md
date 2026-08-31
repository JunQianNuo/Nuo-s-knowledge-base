---
title: playwright-cli
type: Skill
status: 已安装
date: 2026-06-12
---

# playwright-cli

浏览器自动化 CLI，通过命令行操控 Chromium/Firefox/WebKit。

## 完整功能

### 安装

```bash
npm install -g @playwright/cli@latest
# 或本地
npx playwright-cli --version
```

### 命令分类

**核心操作**：`open`、`goto`、`click`、`dblclick`、`type`、`fill`、`drag`、`drop`、`hover`、`select`、`upload`、`check`/`uncheck`、`snapshot`、`eval`、`dialog-accept`/`dialog-dismiss`、`resize`、`close`

**导航**：`go-back`、`go-forward`、`reload`

**键盘**：`press`、`keydown`、`keyup`（支持组合键）

**鼠标**：`mousemove`、`mousedown`/`mouseup`（含右键）、`mousewheel`

**截图导出**：`screenshot`（含元素截图、自定义文件名）、`pdf`

**标签页**：`tab-list`、`tab-new`、`tab-close`、`tab-select`

**存储管理**：
- Cookies：`cookie-list`/`get`/`set`/`delete`/`clear`
- LocalStorage：`localstorage-list`/`get`/`set`/`delete`/`clear`
- SessionStorage：`sessionstorage-list`/`get`/`set`/`delete`/`clear`
- 状态：`state-save`/`state-load`

**网络**：`route`（mock 请求）、`route-list`、`unroute`

**DevTools**：`console`、`requests`、`run-code`、`tracing-start`/`stop`、`video-start`/`stop`

### 浏览器与会话

```bash
playwright-cli open --browser=chrome|firefox|webkit|msedge
playwright-cli open --persistent --profile=/path
playwright-cli attach --cdp=chrome|msedge
playwright-cli attach --cdp=http://localhost:9222
playwright-cli -s=mysession open ...
playwright-cli list / close-all / kill-all
```

### 元素定位

- **ref**（snapshot 返回的引用）— 默认推荐
- CSS 选择器 `"#main > button.submit"`
- Playwright locator `"getByRole('button', { name: 'Submit' })"`

### 参考文件

`references/playwright-tests.md`、`references/request-mocking.md`、`references/running-code.md`、`references/session-management.md`、`references/spec-driven-testing.md`、`references/storage-state.md`、`references/test-generation.md`、`references/tracing.md`、`references/video-recording.md`
