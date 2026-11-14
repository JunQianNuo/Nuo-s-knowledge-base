# Git 与 SSH 配置入门

本教程带你完成四件事：**打开终端 → 安装 Git → 配置 Git 身份 → 配置 SSH 公钥**，最后克隆课程仓库。

## 1. 打开终端（命令行窗口）

不同操作系统打开终端的方式：

| 系统 | 打开方式 |
|---|---|
| Windows | 按 `Win` 键，输入 `PowerShell` 或 `Terminal` 回车（Windows 11 自带 Terminal） |
| macOS | 按 `Cmd+空格` 输入 `Terminal`（终端）回车；或在"启动台 → 其他"里打开 |
| Linux（Ubuntu） | 按 `Ctrl+Alt+T` |

> Windows 上如果使用 WSL2（Ubuntu），也可以在 Ubuntu 终端里操作，命令和 Linux 一致。

## 2. 安装 Git

| 系统 | 安装方法 |
|---|---|
| Windows | 直接下载华为云镜像安装包：[Git-2.55.0.5-64-bit.exe](https://mirrors.huaweicloud.com/git-for-windows/v2.55.0.windows.5/Git-2.55.0.5-64-bit.exe)（多数电脑选 64 位；ARM 芯片的 Windows 笔记本选 [arm64 版](https://mirrors.huaweicloud.com/git-for-windows/v2.55.0.windows.5/Git-2.55.0.5-arm64.exe)）；下载后一路默认"下一步"；装完**重新打开终端**。网络好的话也可用 `winget install Git.Git` |
| macOS | 终端执行 `xcode-select --install`，按提示安装命令行工具（自带 Git）；或 `brew install git` |
| Linux（Ubuntu/Debian） | `sudo apt update && sudo apt install -y git`（默认源即可；速度慢可先配置清华/阿里 apt 镜像源） |

安装完成后验证：

```bash
git --version
```

能输出版本号即安装成功。

> 提示：Git 官方下载站（git-scm.com）的安装包托管在 GitHub，国内下载可能很慢或失败，请使用上面表格里的华为云镜像链接。

## 3. 配置 Git 身份（第一次使用必做）

```bash
git config --global user.name "你的姓名拼音"
git config --global user.email "你的邮箱"
```

这两项会显示在你的提交记录里，请使用你自己的名字和邮箱（例如 `zhangsan` / `zhangsan@uestc.edu.cn`）。

## 4. 配置 SSH 公钥（用于免密克隆与推送）

1. **生成密钥**（一路回车即可，不设置密码也可以）：

   ```bash
   ssh-keygen -t ed25519 -C "你的邮箱"
   ```

2. **查看并复制公钥**：

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

   复制输出的一整行（以 `ssh-ed25519` 开头）。

3. **添加到 Gitee**：登录 [Gitee](https://gitee.com) → 右上角头像 →「设置」→「SSH 公钥」→ 粘贴 → 保存。

4. **验证是否成功**：

   ```bash
   ssh -T git@gitee.com
   ```

   看到 `Hi, xxx! You've successfully authenticated...` 即配置成功。

### Windows 用户特别说明

- 使用 Windows 本地 VS Code 进入课程容器时，在 **Windows PowerShell** 中配置密钥和系统 SSH agent。若未安装 OpenSSH 客户端，按下文 Windows 步骤安装；
- 公钥位置在 `C:\Users\你的用户名\.ssh\id_ed25519.pub`，用 `cat ~/.ssh/id_ed25519.pub` 查看即可；
- Windows 与 WSL 的用户目录、SSH 配置和 agent 环境不同；在 WSL 中启动 agent，不会自动配置 Windows 本地 VS Code 使用的系统 agent。本教程下面的 Windows 步骤使用 Windows 本地 VS Code 与 PowerShell；
- 提示找不到 `ssh-keygen`：先按下文 Windows 步骤安装 OpenSSH Client，重新打开 PowerShell，再用 `Get-Command ssh-keygen` 验证系统 OpenSSH 工具是否可用。

> 常见问题：公钥文件不存在？先执行第 1 步生成；提示 `Permission denied`？检查公钥是否已粘贴到 Gitee，或密钥与 Gitee 账号是否对应。

## 5. 克隆课程仓库

> **先想好把仓库放在哪里**：建议专门建一个课程文件夹（如 `C:\Users\你的用户名\courses` 或 `D:\courses`），课程文件集中存放，方便查找；路径尽量用英文，避免中文和空格，减少个别工具出问题的可能。不要在桌面、下载文件夹等位置直接克隆。

Windows（PowerShell）操作示例：

```powershell
cd C:\Users\你的用户名
mkdir courses
cd courses
git clone git@gitee.com:wenyu-lei/parallel-and-distributed-computing.git
cd parallel-and-distributed-computing
```

macOS / Linux 操作示例：

```bash
mkdir -p ~/courses
cd ~/courses
git clone git@gitee.com:wenyu-lei/parallel-and-distributed-computing.git
cd parallel-and-distributed-computing
```

最省事的方法：在文件资源管理器里先建好并打开这个文件夹，在空白处右键 → "Open Git Bash here"（Windows），再执行克隆。

- SSH 配置不顺利时，可在 Gitee 仓库页面下载 ZIP，用于阅读和运行部分课程内容；Git Pull Request 实验仍需 Git 克隆与认证；
- 克隆/解压完成后，用 VS Code 打开该文件夹，按 `Ctrl+Shift+P`（Mac 为 `Cmd+Shift+P`），输入 `Reopen in Container` 回车，进入课程环境。

> 下载 ZIP 可用于阅读课程文件，但没有 Git 历史与远程仓库配置。要完成 [Git 提交与 Pull Request 实验](../git-practice/README.md)，请用 Git 克隆课程仓库。

## 在 Dev Container 中使用 Git 与 SSH

课程 Dev Container 中可运行 Git。若要从容器中克隆并推送个人 Fork，先在**宿主机**配置 Gitee 公钥和 SSH agent。SSH agent 为 SSH 认证提供已加载的密钥；VS Code Dev Containers 会转发宿主机运行中的 agent，并在容器启动时复制宿主机的 Git 身份配置。私钥保留在宿主机，不要复制到课程仓库或容器中。

**宿主机就是运行 Docker 与本地 VS Code 的电脑。**以下 macOS、Windows 步骤都先在这台电脑的系统终端执行；最后再回到容器验证。密钥路径以第 4 节生成的现有私钥为准，`ssh-add` 使用不带 `.pub` 的私钥文件。

### macOS：打开宿主机终端并准备 agent

按 **`Cmd+空格`**，搜索 **Terminal（终端）**并打开，即进入宿主机终端。macOS 通常已有 SSH agent，先检查：

```bash
ssh-add -l
```

| 输出 | 含义与下一步 |
|---|---|
| 列出密钥指纹 | agent 已运行且有密钥，可继续验证 Gitee 认证。 |
| `The agent has no identities` | agent 已运行，加载下面的现有密钥即可。 |
| `Could not open a connection to your authentication agent` | 当前终端不能连接 agent，按下面的命令启动。 |

若 agent 已运行但没有密钥，执行：

```bash
ssh-add ~/.ssh/id_ed25519
ssh-add -l
ssh -T git@gitee.com
```

若提示无法连接 agent，在**同一个宿主机终端**执行：

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
ssh -T git@gitee.com
```

如果私钥设有口令，`ssh-add` 会要求输入该口令；输入时终端通常不显示字符。

**执行 `eval` 新建 agent 后，需要让 VS Code 继承新的环境。**保存文件，按 **`Cmd+Q` 完全退出所有 VS Code 窗口**，然后在刚才同一个终端进入课程仓库目录并启动 VS Code。以下路径对应第 5 节的示例；仓库在其他位置时改用自己的实际路径：

```bash
cd ~/courses/parallel-and-distributed-computing
code .
```

新 agent 的连接地址 `SSH_AUTH_SOCK` 只设置在当前终端及其后续子进程中；已经运行的 VS Code 不会自动取得它。只关闭一个窗口、执行 Reload Window 或另开一个 VS Code 窗口，不能保证更新这项环境。若只是给原有 agent 加入密钥，通常无需完全退出 VS Code。

若提示 `code: command not found`，VS Code 安装在“应用程序”目录时，可在**刚才同一个宿主机终端**改用启动器的完整路径：

```bash
"/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" .
```

执行前仍需用 `Cmd+Q` 完全退出 VS Code；若应用程序位于其他目录，改用对应路径。也可在 VS Code 命令面板安装 **Shell Command: Install 'code' command in PATH**；安装后再次完全退出 VS Code，返回原先准备 agent 的终端启动，以保留新的 `SSH_AUTH_SOCK`。

### Windows：启动系统服务并加载本人密钥

本节适用于 **Windows 10/11 上的本地 VS Code**。使用 Windows OpenSSH 的系统 `ssh-agent` 服务；Git Bash 或 WSL 中另行启动的 agent 不是这个系统服务。以下服务命令在 Windows PowerShell 中执行。

**第一步：管理员 PowerShell 管理服务。**按 `Win`，搜索 **PowerShell**，选择 **以管理员身份运行**，执行：

```powershell
Set-Service -Name ssh-agent -StartupType Automatic
Start-Service ssh-agent
Get-Service ssh-agent
```

最后的服务状态应为 **`Running`**。如果提示“拒绝访问”，检查当前 PowerShell 是否以管理员身份运行。

若提示找不到 `ssh-agent` 服务，先在管理员 PowerShell 安装 **OpenSSH Client（客户端）**，安装成功后再执行上面的服务命令：

```powershell
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```

这里使用客户端连接 Gitee，配置的是 `ssh-agent` 服务，无需安装 OpenSSH Server 或启动 `sshd`。

**第二步：本人普通 PowerShell 加载密钥。**关闭管理员窗口，按 `Win` 搜索 PowerShell 并正常打开，使用与运行 VS Code 相同的 Windows 账号，执行：

```powershell
ssh-add "$env:USERPROFILE\.ssh\id_ed25519"
ssh-add -l
ssh -T git@gitee.com
```

`$env:USERPROFILE` 是当前 Windows 用户目录，例如 `C:\Users\zhangsan`。若管理服务时使用了另一个管理员账号，仍应回到本人账号加载自己的密钥。密钥已有口令时，按提示输入。

如果服务已经是 `Running`，但 `ssh-add` 仍无法连接 agent，检查实际调用的工具：

```powershell
Get-Command ssh-add
```

若调用到了其他安装目录中的 SSH 工具，可显式使用 Windows OpenSSH 加载并检查：

```powershell
& "$env:WINDIR\System32\OpenSSH\ssh-add.exe" "$env:USERPROFILE\.ssh\id_ed25519"
& "$env:WINDIR\System32\OpenSSH\ssh-add.exe" -l
& "$env:WINDIR\System32\OpenSSH\ssh.exe" -T git@gitee.com
```

服务运行、本人密钥加载且 Gitee 认证成功后，保存文件并退出所有 VS Code 窗口，再以本人账号打开课程仓库。

### 回到容器：验证转发与 Git 身份

在 VS Code 按 **`Cmd+Shift+P`（macOS）**或 **`Ctrl+Shift+P`（Windows）**，选择 **Dev Containers: Reopen in Container**。进入容器后新建一个终端，执行：

```bash
ssh-add -l
ssh -T git@gitee.com
git config --global user.name
git config --global user.email
```

`ssh-add -l` 应列出与宿主机对应的密钥指纹；`ssh -T` 应返回本人 Gitee 账号的认证成功提示。Gitee 不提供交互式 shell，成功提示可能伴随非零退出码，以认证提示为准。

全局 Git 姓名和邮箱若为空，可在个人 Fork 的克隆目录设置本地身份：

```bash
git config --local user.name "你的姓名拼音"
git config --local user.email "你的邮箱"
git config user.name
git config user.email
```

最后两条命令显示该仓库提交时实际使用的身份。

### 常见问题

| 现象 | 处理 |
|---|---|
| 容器中 `The agent has no identities` | 回宿主机把本人已有私钥加入 agent，再回容器检查。 |
| 容器中无法连接 agent | 先在宿主机确认 agent 可用；macOS 手动新建 agent 后从同一终端重启 VS Code，再重新打开容器。Windows 确认系统服务为 `Running`。 |
| 私钥路径不存在 | 核对第 4 节使用的文件名和用户目录；已有密钥时使用它的实际路径。只有尚未生成密钥时才执行第 4 节。 |
| `Permission denied (publickey)` | 检查 agent 中的密钥，以及对应的 `.pub` 公钥是否登记到本人 Gitee 账号。先在宿主机认证成功，再检查容器。 |
| 宿主机认证成功、容器认证失败 | 核对两边 `ssh-add -l` 的指纹，检查 VS Code 的启动环境和当前 Windows 账号，然后重新打开容器。 |

Linux 用户可在宿主机终端使用 `eval "$(ssh-agent -s)"` 与 `ssh-add` 准备 agent；若新建了 agent，同样从该终端重新启动 VS Code，再按上面的容器验证步骤检查。

## 6. 常用命令速查

| 命令 | 作用 |
|---|---|
| `git status` | 查看工作区状态 |
| `git log --oneline` | 查看提交历史 |
| `git remote -v` | 查看远程仓库地址与名称 |
| `git checkout -b 分支名` | 创建并切换到新分支 |
| `git diff` | 查看未提交的改动 |
| `git add 文件名` | 把修改加入暂存区 |
| `git diff --cached` | 查看已暂存、即将提交的改动 |
| `git commit -m "说明"` | 提交到本地 |
| `git push -u origin 分支名` | 把本地分支推送到自己的 Fork |
| `git pull` | 拉取远程更新 |
| `git checkout -- 文件名` | 丢弃某文件未提交的修改（慎用） |

不熟悉命令行的话，VS Code 左侧的「源代码管理」图标也可以完成 add/commit 等操作。

完整的 Fork、分支、提交与 Pull Request 流程见 [Git 提交与 Pull Request 实验](../git-practice/README.md)。

## 参考资料

- [VS Code Dev Containers：Sharing Git credentials with your container](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials)：宿主机 agent 转发、Windows 服务启动与 Git 配置共享。
- [VS Code：Environment variables between VS Code instances](https://code.visualstudio.com/docs/terminal/advanced#environment-variables-between-vs-code-instances)：VS Code 实例继承启动环境的方式。
- [VS Code：Launch VS Code from the command line on macOS](https://code.visualstudio.com/docs/setup/mac#launch-vs-code-from-the-command-line)：安装 `code` 命令并从终端启动。
- [Microsoft Learn：Key-based authentication in OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement)：系统 `ssh-agent` 服务与用户密钥管理。
- [Microsoft Learn：Get started with OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse)：安装 OpenSSH Client。
- [OpenSSH：ssh-agent](https://man.openbsd.org/ssh-agent.1)、[ssh-add](https://man.openbsd.org/ssh-add.1)：agent 环境变量、密钥加载与指纹检查。

上述 SSH agent 操作资料核对日期：2026-10-11。
