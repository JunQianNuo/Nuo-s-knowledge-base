---
title: Lark（飞书）Skills
type: Skill
status: 已安装
source:
  - plugin: lark-cli
date: 2026-06-12
---

# Lark（飞书）Skills

飞书生态全套 Agent Skills，基于 `lark-cli`，通过 Shortcuts（`+` 命令）操作飞书各项服务。

## 子 Skills 一览

### lark-im — 即时通讯

**Shortcuts**：`+chat-create`、`+chat-list`、`+chat-search`、`+chat-update`、`+chat-messages-list`、`+messages-mget`、`+messages-reply`、`+messages-send`、`+messages-search`、`+messages-resources-download`、`+threads-messages-list`、`+flag-create`/`+flag-cancel`/`+flag-list`

**核心能力**：收发消息（text/markdown/post/media/card）、群聊管理（创建/搜索/更新/成员增删）、话题回复、表情反应、书签标记、图片文件上传下载（大文件分片 8MB 块）、消息搜索（关键词/发送者/时间范围）、消息转发（单条/合并）、应用内/短信/电话加急

**API 资源**：`chats`、`chat.members`、`messages`（含 `delete`/`forward`/`merge_forward`/`urgent_app`/`urgent_phone`/`urgent_sms`）、`reactions`、`threads`、`images`、`pins`

### lark-doc — 云文档 (v2 API)

**Shortcuts**：`+create`、`+fetch`、`+update`、`+media-insert`、`+media-download`、`+media-preview`

**核心能力**：
- **读取**：`+fetch --api-version v2` 支持按 scope/detail 选择、局部读取（block ID 定位）、XML/Markdown 输出
- **创建**：XML（支持 callout/grid/checkbox 等富 block）或 Markdown 格式
- **编辑**：`str_replace` / `block_insert_after` / `block_replace` / `block_delete` / `block_move_after` 精准局部精修
- **媒体**：插入本地图片/文件（含剪贴板直传）、下载文档素材/画板缩略图、预览素材
- **嵌入识别**：自动提取 `<sheet>`/`<bitable>` 等嵌入标签的 token 并切到对应技能下钻

**格式规则**：创建/整段写入可选 XML 或 Markdown；精准编辑优先 XML（能稳定表达 block 结构和样式）

### lark-base — 多维表格 (Base/bitable)

**Shortcuts**：`+base-get`/`+base-create`/`+base-copy`、`+base-block-list`/`+base-block-create`/`+block-move`/`+block-rename`/`+block-delete`、`+table-*`（list/get/create/update/delete）、`+field-*`（list/get/create/update/delete/search-options）、`+record-*`（get/list/search/upsert/batch-create/batch-update/delete/upload-attachment/download-attachment/remove-attachment/share-link-create/history-list）、`+view-*`、`+data-query`、`+form-*`、`+dashboard-*`/`+dashboard-block-*`、`+workflow-*`、`+advperm-*`/`+role-*`

**核心能力**：
- **表管理**：创建/复制/删除数据表，管理 Base 内资源目录（folder/table/docx/dashboard/workflow）
- **字段管理**：创建/更新公式字段（`formula`）、关联字段（`lookup`）等，含完整 JSON DSL
- **记录操作**：批量增删改查（单批最多 200 条）、附件上传下载移除、分享链接、历史追溯
- **数据查询**：`+record-list`/`+record-search` 做原始记录查询（filter/sort）；`+data-query` 做聚合统计
- **视图管理**：筛选/排序/分组/卡片/甘特/日历视图配置
- **表单**：提交表单、创建/更新表单题目、管理表单
- **仪表盘**：创建管理 dashboard block，含 `data_config` DSL；`+dashboard-block-get-data` 读取图表计算结果
- **工作流**：创建/启停 workflow，含 steps JSON SSOT
- **权限**：高级权限与自定义角色管理

**关键约束**：写入前必须先读字段结构；公式/lookup 字段只读；跨表先读目标表结构；`has_more=true` 不能做全局结论

### lark-calendar — 日历与日程 (v4)

**Shortcuts**：`+agenda`、`+create`、`+update`、`+freebusy`、`+room-find`、`+rsvp`、`+suggestion`

**核心能力**：
- **日程管理**：创建/编辑/删除单次或重复性日程（RFC5545 iCalendar 标准）
- **会议预约**：智能助理模式——能补全的默认值先补全，只在时间冲突/无法确定时才追问
- **会议室**：`+room-find` 按时间块查询可用会议室；`+suggestion` 推荐可用时间块
- **忙闲查询**：`+freebusy` 查询用户忙闲状态和 RSVP 状态
- **重复日程**：支持对重复日程的具体实例操作（编辑某次/删除某次/调整参会人/更换会议室）
- **参会人**：增量添加/移除参会人和会议室

**硬性约束**：涉及预约/会议室必须先读 `lark-calendar-schedule-meeting.md`；无明确时间禁止直接 `+room-find`；操作后验证需等 2 秒同步延迟

### lark-sheets — 电子表格

创建操作电子表格、管理工作表与行列结构（增删/合并/调整尺寸/隐藏/冻结）、读写单元格（值/公式/样式/批注/图片）、查找替换、批量更新、图表、透视表、条件格式、筛选器、迷你图、浮动图片

### lark-slides — 幻灯片

创建和编辑演示文稿（XML 协议），管理幻灯片页面（创建/删除/读取/局部替换）

### lark-vc — 视频会议

搜索历史会议（按关键词/时间/组织者/参会人/会议室）、获取会议纪要产物（总结/待办/章节/逐字稿）、查询参会人快照

### lark-vc-agent — 会议机器人

机器人代用户加入/离开进行中会议、读取会中实时事件（参会人加入离开/发言/聊天/屏幕共享）

### lark-minutes — 妙记

查询妙记列表、获取基础信息（标题/封面/时长）、下载音视频文件、获取 AI 产物（总结/待办/章节）、上传音视频生成妙记、替换逐字稿说话人

### lark-mail — 邮箱

起草/发送/回复/转发/搜索邮件、管理草稿/文件夹/标签/联系人/附件/邮件规则、监听新邮件

### lark-contact — 通讯录

按姓名/邮箱解析 open_id、按 open_id 反查姓名/部门/邮箱/联系方式/个人状态/签名

### lark-drive — 云空间

上传下载文件、创建文件夹、复制/移动/删除文件、查看元数据、管理评论和权限、修改文件标题、导入本地文件为在线文档

### lark-wiki — 知识库

管理知识空间、空间成员和文档节点层级结构，在知识库中组织文档和快捷方式

### lark-approval — 审批

审批实例查询、审批任务管理

### lark-task — 任务

创建待办、查看更新任务状态、拆分子任务、组织清单、分配协作成员、上传附件、注册/注销任务智能体

### lark-okr — OKR

管理目标与关键结果、查看编辑周期/对齐关系/量化指标/进展记录

### lark-attendance — 考勤

查询考勤打卡记录

### lark-event — 事件订阅

实时监听飞书事件流（IM 消息/反应/群变更、VC 会议结束、妙记生成等），NDJSON 流式输出

### lark-markdown — Markdown

查看、创建、上传、编辑和比较 Markdown 文件

### lark-whiteboard — 画板

查询编辑飞书画板、导出预览图片/原始节点结构、用 DSL/PlantUML/Mermaid 更新画板内容

### lark-apps — 妙搭

本地 HTML 文件或目录部署为飞书妙搭应用，生成公网可访问链接

### lark-openapi-explorer — OpenAPI 探索

从官方文档库查找未封装的原生 OpenAPI 接口，供 lark-cli 未覆盖的需求使用

### lark-shared — 全局

认证登录、身份切换（`--as user`/`--as bot`）、权限 scope 处理、lark-cli 升级

### lark-skill-maker — Skill 制作

封装飞书 API 操作为可复用自定义 Skill

### lark-workflow-meeting-summary — 会议纪要整理

汇总指定时间范围内会议纪要并生成结构化报告

### lark-workflow-standup-report — 日程待办摘要

编排 `+agenda` 和 `task +get-my-tasks`，生成指定日期日程与未完成任务摘要
