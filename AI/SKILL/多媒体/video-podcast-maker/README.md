---
title: video-podcast-maker
type: Skill
status: 已安装
date: 2026-06-12
---

# video-podcast-maker

4K Bilibili 横屏知识视频自动化 pipeline：研究→脚本→TTS→Remotion→MP4+BGM。

## 完整功能

### 15 步工作流

| 步骤 | 产出 |
|------|------|
| 1. 定义主题方向 | `topic_definition.md` |
| 2. 研究主题 | `topic_research.md` |
| 3. 设计 5-7 段落 | 内存中 |
| 4. 写旁白脚本 | `podcast.txt` |
| 4.5 中文发音预检 | `phonemes.json` |
| 5. 收集媒体素材（Auto 模式跳过） | `media_manifest.json` |
| 6. 生成发布信息（Part 1） | `publish_info.md` |
| 7. 生成缩略图（16:9 + 4:3） | `thumbnail_*.png` |
| 8. 生成 TTS 音频 | `podcast_audio.wav` + `timing.json` |
| **9. Remotion 合成 + Studio 预览** | 必须启动 `npx remotion studio` 等反馈 |
| 10. 渲染 4K（仅用户确认后） | `output.mp4` |
| 11. 混入背景音乐 | `video_with_bgm.mp4` |
| 12. 最终化（可选字幕烧录） | `final_video.mp4` |
| 13. 完善发布信息（Part 2） | 章节时间戳 |
| **14. 验证输出** | `verify_output.py` 必须通过 |
| 15. 生成竖屏短视频（可选） | `shorts/` |

### 硬性规则

| 规则 | 要求 |
|------|------|
| **单项目** | 所有视频在 `videos/{name}/` 下，不新建项目 |
| **4K 输出** | 3840×2160，`scale(2)` 包裹 1920×1080 设计空间 |
| **音频同步** | 所有动画由 `timing.json` 驱动 |
| **缩略图** | 必须生成 16:9 + 4:3 两种 |
| **Studio 先于渲染** | 必须启动 `remotion studio` 预览，用户确认后才渲染 |
| **`--public-dir`** | 每个 Remotion 命令必须加 `--public-dir videos/{name}/` |

### 输出规格

| 参数 | 横屏 (16:9) | 竖屏 (9:16) |
|------|------------|------------|
| 分辨率 | 3840×2160 (4K) | 2160×3840 (4K) |
| 帧率 | 30 fps | 30 fps |
| 编码 | H.264, 16Mbps | H.264, 16Mbps |
| 音频 | AAC, 192kbps | AAC, 192kbps |
| 时长 | 1-15 分钟 | 60-90 秒 |

### 执行模式

- **Auto 模式**（默认）：全自动 pipeline，Step 9 强制停在 Studio
- **Interactive 模式**：每步决策点询问用户

### 依赖

- Remotion（含 `remotion-best-practices` skill）
- TTS 后端（Azure/Edge 等，自动检测）
- FFmpeg
