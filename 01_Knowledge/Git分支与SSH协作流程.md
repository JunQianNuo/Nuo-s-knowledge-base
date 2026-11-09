---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-并行与分布式计算]]'
source:
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-12-第12节-MPI并行计算与Git版本控制课程宣讲]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-14-第13节-Git与MPI编程教学]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-09-30-第10节-OpenMP并行编程培训]]'
- '[[03_Sources/Courses/并行与分布式计算/课堂笔记/2026-10-19-第14节-MPI通信与并行计算培训]]'
---
# Git分支与SSH协作流程

> 一句话：用 SSH 证明访问身份，用 Git 分支保存一组可审查修改，再把分支推到远端提交 Pull Request。

## 适用条件

已有代码托管账户和访问权限，需要在团队仓库上完成一次独立修改。课程要求先 fork 时，先在平台生成自己的仓库副本，再克隆它；fork 是平台上的仓库关系，clone 是取到本地，二者不同。

## 从身份配置到提交审查

1. 用 `ssh-keygen -t ed25519` 生成密钥；已有可用密钥可复用。把公钥文件（通常以 `.pub` 结尾）添加到平台账户，私钥留在本地，不上传、不写进仓库。
2. 使用平台给出的实际 SSH 地址克隆。下面的 `host`、`account` 和仓库名都是待替换值。

```bash
git clone git@host:account/repository.git
cd repository
git checkout -b feature-name
```

3. 修改后先看状态和差异，再逐文件暂存；提交前检查暂存内容，避免把无关文件或敏感信息一起提交。

```bash
git status
git diff
git add path/to/file
git diff --cached
git commit -m "Describe the change"
git push --set-upstream origin feature-name
```

4. 在平台创建 Pull Request，核对源仓库、源分支和目标分支，说明问题、修改行为与验证结果。首次推送的 `--set-upstream` 建立本地分支与远端分支的关联，之后可按该关联执行 `git push`。

## 冲突与完成标准

冲突表示两边修改无法自动合并。读懂冲突区域和双方意图，保留正确组合，清除冲突标记后运行相应检查，再暂存并完成当前合并或变基流程。只删除标记无法证明代码正确。

本地 `commit` 不代表远端已收到；`push` 不代表 Pull Request 已合并。最终检查平台上的分支提交和 PR 目标是否正确。本卡记录可复用流程，来源中的具体作业路径、平台和考核安排仍以原课堂记录为准。
