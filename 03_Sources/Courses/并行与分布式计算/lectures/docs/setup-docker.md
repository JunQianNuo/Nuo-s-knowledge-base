# 环境搭建：Docker + VS Code Dev Container（统一推荐路线）

目标：在你自己的电脑上用 VS Code 打开课程仓库并"在容器中重新打开"，即可获得与老师完全一致的 Linux 实验环境（GCC + OpenMP + OpenMPI + 常用工具）。

## 前置要求

- 64 位操作系统：Windows 10/11、macOS 或主流 Linux 发行版；
- 至少 4 GB 可用内存（推荐 8 GB）；
- 磁盘剩余空间 10 GB 以上；
- 网络可访问阿里云容器镜像服务（国内网络即可）。

## 第 1 步：安装 Docker

### Windows

1. 启用 WSL2：以管理员身份打开 PowerShell，执行

   ```powershell
   wsl --install
   ```

   然后重启电脑。Docker Desktop 在 Windows 上依赖 WSL2，这一步会自动装好。

2. 下载安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)；
3. 启动 Docker Desktop，确认 Settings → General 中勾选 "Use the WSL 2 based engine"；
4. **启用 WSL 集成（重要）**：Settings → Resources → WSL Integration，勾选 "Enable integration with my default WSL distro" 和 **Ubuntu**，点 Apply & Restart；
5. 验证：在 PowerShell 中执行 `docker --version` 能输出版本号即可。

> 如果在"在容器中重新打开"时报错 `accessing specified distro mount service: stat /run/guest-services/distro-services/ubuntu.sock: no such file or directory`，说明 Dev Containers 自动挂载 Wayland socket 失败。按 [FAQ](faq.md) 中的对应条目处理（关闭 Wayland socket 挂载即可）。

### macOS

1. 下载安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)（Apple Silicon 芯片会自动选择对应架构）；
2. 启动后在 Settings → Resources 中给 Docker 分配至少 4 GB 内存；
3. 验证：终端执行 `docker --version`。

### Linux（Ubuntu/Debian 为例）

```bash
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker $USER
```

注销并重新登录（或执行 `newgrp docker`），然后验证 `docker --version`。

## 第 2 步：安装 VS Code 与扩展

1. 安装 [VS Code](https://code.visualstudio.com/)；
2. 在扩展市场搜索并安装 **Dev Containers**（发布者 ms-vscode-remote）；
3. 建议同时安装 **C/C++ Extension Pack**，获得代码补全与调试支持。

## 第 3 步：获取课程仓库

> **先想好把仓库放在哪里**：建议专门建一个课程文件夹（如 `C:\Users\你的用户名\courses`，路径用英文），先进入该文件夹，再执行下面的克隆；不要直接克隆到桌面或下载文件夹。

方式一（推荐，需要 Git）：

```bash
git clone git@gitee.com:wenyu-lei/parallel-and-distributed-computing.git
```

第一次用 Git 的同学，先看 [Git 与 SSH 配置入门](git-入门.md)，里面有各系统打开终端、安装配置 Git、设置 SSH 公钥的详细步骤。

方式二：在 Gitee 仓库页面点「下载 ZIP」，解压到本地。

## 第 4 步：在容器中打开

> VS Code 更新后，左下角的远程状态图标样式/颜色可能因版本而异，因此统一使用**命令面板**方式打开，各版本通用。

1. 用 VS Code 打开仓库文件夹；
2. 按 `Ctrl+Shift+P`（Mac 为 `Cmd+Shift+P`）打开命令面板；
3. 输入 `Reopen in Container`，选择 **Dev Containers: Reopen in Container** 并回车；
4. 首次打开会拉取课程基础镜像，并按 `.devcontainer/Dockerfile.debug` 安装 GDB/gdbserver；需要访问课程镜像仓库和 Ubuntu 软件源，后续可复用本地构建缓存；
5. 状态栏出现容器提示（如左下角显示 "Dev Container"）后，打开内置终端（`Ctrl+``），即进入 Linux 环境。

如果没有出现 "Dev Containers" 相关命令，说明 **Dev Containers 扩展未安装**，回到第 2 步安装扩展后重试。

## 第 5 步：环境自检

在 VS Code 内置终端执行：

```bash
bash scripts/check_env.sh
```

把完整输出贴给老师，即完成实验一的环境部分。

## 常见问题

安装或拉取镜像遇到问题，先查 [FAQ](faq.md)。

## 更新 MPI 调试工具

第 9.5 讲需要 GDB/gdbserver。更新仓库配置后，在命令面板运行 **Dev Containers: Rebuild Container**，仍使用普通用户 student。在容器中运行 `bash examples/mpi/09a_mpi_debug/scripts/check_debug.sh`；具体双进程操作见 [MPI 调试实验](../examples/mpi/09a_mpi_debug/README.md)。无需在 Mac/Windows 宿主机另装 GDB，也无需发布调试端口。
