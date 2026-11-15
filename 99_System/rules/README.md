# 规范入口

这里保存知识库当前使用的写作、课程处理与质量检查规范。按任务读取对应文件；通用操作见 [[docs/USAGE]]。

## 现行依据

- 新内容属性采用 `99_System/knowledge/v2/schemas/`，模板使用 `99_System/knowledge/v2/templates/`；不要用 v1 Registry 或正文中的旧示例覆盖 v2。
- 各规范中非冲突的内容与质量要求继续适用。历史目录示例不构成移动、删除或自动升级授权。
- 规则文档属于 System，不计入知识原子、来源实体或主题统计；原有维护程序与内部状态不变。

## 任务规范

- [[99_System/rules/Obsidian写作规范|Obsidian写作规范]]
- [[99_System/rules/习题库规范|习题库规范]]
- [[99_System/rules/知识原子卡规范|知识原子卡规范]]
- [[99_System/rules/知识库元数据规范|知识库元数据规范]]
- [[99_System/rules/考试复习规范|考试复习规范]]
- [[99_System/rules/课堂录音归档规范|课堂录音归档规范]]
- [[99_System/rules/课程笔记生成规范|课程笔记生成规范]]
- [[99_System/rules/质量审查规范|质量审查规范]]
- [[99_System/rules/闪卡规范|闪卡规范]]

## 配套工具

PDF 导出脚本位于 `99_System/tools/export_pdfs.py`，以显式传入的目录为处理对象；迁移未执行 PDF 导出。
