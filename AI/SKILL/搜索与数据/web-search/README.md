---
title: web-search
type: Skill
status: 已安装
date: 2026-06-12
---

# web-search

Brave Search API 封装，结构化网页搜索。

## 完整功能

### 端点

```bash
GET/POST https://api.search.brave.com/res/v1/web/search
Header: X-Subscription-Token: ${BRAVE_SEARCH_API_KEY}
```

### 核心参数

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| `q` | string | 必填 | 搜索查询（1-400字符，最多50词） |
| `country` | string | `US` | 2字母国家码或 `ALL` |
| `search_lang` | string | `en` | 语言偏好 |
| `count` | int | `20` | 每页结果数（1-20） |
| `offset` | int | `0` | 分页偏移（0-9） |
| `safesearch` | string | `moderate` | `off`/`moderate`/`strict` |
| `freshness` | string | — | `pd`/`pw`/`pm`/`py` 或日期范围 |

### 结果类型

| 类型 | 内容 |
|------|------|
| `web` | 网页（标题/URL/摘要/缩略图/发布时间） |
| `news` | 新闻 |
| `videos` | 视频（时长/播放量/创作者） |
| `discussions` | 论坛讨论（问题/回复数/热评） |
| `faq` | FAQ |
| `infobox` | 知识图谱 |
| `locations` | 本地 POI |

### 结构化数据（schemas 字段）

自动提取 schema.org 数据：`product`、`recipe`、`article`、`book`、`software`、`rating`、`movie`、`video`、`organization`、`review`、`music_recording`

### 搜索运算符

`site:`、`ext:`/`filetype:`、`intitle:`、`inbody:`、`lang:`、`loc:`、`+term`、`-term`、`"exact phrase"`、`AND`/`OR`/`NOT`

### Goggles（自定义排序 — Brave 独有）

通过托管或内联规则重排搜索结果：`$boost=N`/`$downrank=N`（1-10）、`$discard`、`$site=`

### Rich Data 回调

天气/股票/体育/货币等查询可获取结构化富数据（`enable_rich_callback=true` → `rich.hint.callback_key` → `/rich` 端点）

### 位置感知

通过 `X-Loc-Lat`/`X-Loc-Long` 等 Header 获取本地化结果
