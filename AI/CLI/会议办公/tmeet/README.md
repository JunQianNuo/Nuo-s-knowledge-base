---
title: tmeet
type: CLI
status: 已安装
source:
  - npm: "@tencentcloud/tmeet"
date: 2026-09-01
---

# tmeet

腾讯会议命令行工具，支持 OAuth 授权、会议全生命周期管理、录制与转写、会议报告查询。

## 安装与登录

```bash
npm install -g @tencentcloud/tmeet@latest
tmeet auth login   # 阻塞命令，后台运行以捕获授权 URL
tmeet auth status  # 查看登录状态与 Token 有效期
```

## 核心命令

```bash
tmeet record list --start 2026-09-01T00:00:00+08:00 --end 2026-09-30T23:59:59+08:00 --compact
tmeet record address --meeting-record-id <id>                    # 录制下载地址
tmeet record smart-minutes --record-file-id <id> --lang zh       # 智能纪要
tmeet record transcript-paragraphs --record-file-id <id>         # 转写段落列表
tmeet record transcript-get --record-file-id <id> --pid 0 --limit 50  # 转写文本（分页）
tmeet meeting list-ended --start ... --end ...                   # 已结束会议
```

## 自动化

- 课堂录音自动拉取归档：`python scripts/pull_tmeet_recordings.py`（详见 [[规范/课堂录音归档规范|课堂录音归档规范]]）
- 权限申请：`record permission-apply-prepare` → 用户确认 → `record permission-apply-commit`

## 关联

- 规范：[[规范/课堂录音归档规范|课堂录音归档规范]]
- 课表：[[课表|课表]]
