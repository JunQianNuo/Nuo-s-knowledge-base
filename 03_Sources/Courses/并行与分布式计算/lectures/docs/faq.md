# 常见问题（FAQ）

格式：报错/现象 → 原因 → 解决办法。

## 安装阶段

| 报错 / 现象 | 原因 | 解决办法 |
|---|---|---|
| `wsl: command not found` | Windows 版本过旧 | 更新 Windows 到 10 2004+ 或 11 |
| `WSL 2 requires an update to its kernel component` | WSL 内核过旧 | 管理员 PowerShell 执行 `wsl --update` |
| `Please enable the Virtual Machine Platform` / 提示虚拟化未开启 | BIOS 未开启虚拟化 | 重启进 BIOS 开启 Intel VT-x / AMD-V |
| `Docker Desktop requires a newer WSL kernel` | WSL 未更新 | `wsl --update` 后重启 Docker Desktop |
| `docker: command not found` | Docker 未安装或 PATH 未配置 | 重装 Docker Desktop；Windows 上重新登录 |
| Docker Desktop 启动失败 | 内存不足或 WSL 异常 | 重启 Docker Desktop；设置里调大内存；必要时 `wsl --shutdown` 后重试 |

## 拉取镜像与容器阶段

| 报错 / 现象 | 原因 | 解决办法 |
|---|---|---|
| `pull access denied for ...` 或 `repository does not exist` | 镜像地址未发布/写错 | 确认 `.devcontainer/devcontainer.json` 中地址为教师发布的最新地址 |
| `manifest unknown` | 镜像 tag 不存在 | 检查 tag（如 `2026.1`）是否与文档一致 |
| 拉取速度极慢 / 超时 | 网络问题 | 主渠道为阿里云 ACR（国内快）；如仍失败，联系老师获取离线包 |
| `accessing specified distro mount service: stat /run/guest-services/distro-services/ubuntu.sock: no such file or directory` | Dev Containers 自动挂载 WSLg 的 Wayland socket，但 Docker Desktop 与 Ubuntu 的 WSL 集成未启用/服务未运行 | ① Docker Desktop → Settings → Resources → WSL Integration → 勾选 Ubuntu → Apply & Restart；② 仍报错则 PowerShell 执行 `wsl --shutdown` 后重启 Docker Desktop；③ 课程不需要容器内 GUI，可在 VS Code 设置中关闭 "Dev > Containers: Mount Wayland Socket"（settings.json 加 `"dev.containers.mountWaylandSocket": false`） |
| "Reopen in Container" 时提示需要在 WSL 里安装 Docker | 文件夹是从 WSL 侧打开的（左下角显示 "WSL: Ubuntu"，或路径以 `\\wsl.localhost\` 开头），Dev Containers 于是在 WSL 发行版内找 docker 命令，而 Docker Desktop 没有向该发行版注入 CLI。注意：即使选了 `C:\` 路径，只要窗口仍挂在 WSL 上（例如从 WSL 终端用 `code .` 启动过 VS Code），打开目录也仍是 WSL 上下文 | 不要安装提示中的 Docker（会在 WSL 里装一套独立 Docker Engine，与 Docker Desktop 冲突）；关键是获得"本地窗口"：关掉所有 VS Code 窗口，从 Windows 桌面/任务栏图标重新启动（不要从 WSL 终端执行 `code`），或在 PowerShell（非 WSL）执行 `code C:\Users\你的用户名\parallel-and-distributed-computing`；打开后左下角不应出现 "WSL: Ubuntu"，再 Reopen in Container。若确实想用 WSL 方式，先在 Docker Desktop → Resources → WSL Integration 勾选 Ubuntu 并重启。若不慎已点安装（日志出现 `NO_PUBKEY ...` 等 GPG 报错），在 WSL 里执行 `sudo rm -f /etc/apt/sources.list.d/docker.list /etc/apt/keyrings/docker.gpg && sudo apt update` 清理残留软件源即可 |
| `error during connect ... the pipe is closed` | Docker Desktop 未启动 | 先启动 Docker Desktop，再重新打开容器 |
| `Cannot connect to the Docker daemon` | Docker 服务未运行 | Linux 执行 `sudo systemctl start docker`；macOS/Windows 启动 Docker Desktop |
| 容器打开后 VS Code 卡在 "Starting Dev Container" | 首次拉镜像或资源不足 | 耐心等待；查看右下角日志；必要时给 Docker 分配更多内存 |

## 编译与运行阶段

| 报错 / 现象 | 原因 | 解决办法 |
|---|---|---|
| 运行 `bash scripts/check_env.sh` 报 `line 22: $'\r': command not found` 或 `syntax error: unexpected end of file` | Windows 检出代码时把脚本行尾从 LF 转成了 CRLF，bash 不识别 `\r` | 仓库已统一为 LF 行尾，新克隆不会再遇到；已有副本请删除后重新 `git clone`（只转换单个文件可用 `sed -i 's/\r$//' 文件名` 临时应急） |
| `fatal error: omp.h: No such file or directory` | 编译器不支持/未启用 OpenMP | 确认使用 `gcc -fopenmp`；容器内环境默认可用 |
| `unrecognized command-line option '-fopenmp'` | 编译器过旧或不是 GCC | 确认使用容器内环境；gcc 版本至少 4.2 |
| `libgomp.so.1: cannot open shared object file` | 运行库缺失 | 容器内已安装；本机编译需安装 libgomp |
| `mpirun has detected an attempt to run as root` | OpenMPI 禁止 root 运行 | 容器内已使用 `student` 用户；本地请勿用 root |
| 编译通过但输出乱码（Windows） | 终端编码问题 | VS Code 终端设置 UTF-8；或 `chcp 65001` |
| `make: Nothing to be done` | 二进制已是最新 | 先 `make clean` 再 `make` |

## 其他

| 报错 / 现象 | 原因 | 解决办法 |
|---|---|---|
| 磁盘空间不足 | 镜像与容器占用 | 清理：`docker system prune -a`（会删除未使用镜像，慎用） |
| 提示 `ssh-keygen 不是内部或外部命令`（Windows） | OpenSSH 客户端未启用或 Git 未加入 PATH | 重装 Git 并勾选 "Add Git to PATH"；或在「设置 → 应用 → 可选功能」中安装 OpenSSH 客户端 |
| 老师更新了示例 / 作业代码 | 课程文件是实时挂载进容器的，代码更新不需要更新容器 | 在仓库目录执行 `git pull` 即可，已打开的容器里立即可见（推荐在 Windows 侧的 Git Bash / PowerShell 里执行，避免 SSH 密钥未转发导致失败） |
| 老师更新了实验环境（镜像 tag 变化） | 环境组件（编译器、库等）有变化，需要重建容器 | `Ctrl+Shift+P` → "Dev Containers: Rebuild Container"，会自动拉取新镜像，无需重装 Docker |
| 我在容器里改的代码 / 新建的文件，关闭或重建容器后会丢吗 | `/workspace` 是挂载到本机仓库文件夹的，改动会实时保存在你电脑硬盘上，关闭、重开、甚至重建容器都不会丢；但写在容器其他位置（如 `/tmp`、`/home/student`）的文件只存在于容器临时层，执行 "Rebuild Container" 后会被清空 | 课程代码和练习统一放在 `/workspace`（即仓库目录）里；重要内容建议在 Windows 侧用 git 提交（commit）再保存一份 |
| 在容器里执行 `sudo` 报错 / 不知道 sudo 密码 | 课程镜像没有安装 sudo，`student` 用户也未设置密码、不在管理员组，课程环境本身不需要管理员权限 | 所有工具已预装，代码放在 `/workspace` 即可；确需 root 时由老师在 Windows 侧 `docker exec -u root -it <容器名> bash` 临时进入，或联系老师更新镜像 |

仍有问题？把**完整报错信息**和**自检输出**发给老师。
