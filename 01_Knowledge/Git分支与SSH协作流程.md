---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-12-第12节-MPI并行计算与Git版本控制课程宣讲]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-14-第13节-Git与MPI编程教学]]'
---
# Git分支与SSH协作流程

按项目要求fork，再用SSH公钥授权并克隆；私钥保存在本地且不提交。新分支修改，git diff核差异，逐文件add，commit描述变化，首次push建立上游，再创建Pull Request供审查。冲突须理解双方语义后解决并验证，不能只删标记。这里是课程工作流知识，来源中的仓库和考试安排仍留原文，不代表已经推送或提交。
