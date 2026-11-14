# 备选路线：WSL2 直接安装工具链（不装 Docker）

如果你暂时无法安装 Docker Desktop，可以在 Windows 上用 WSL2 + Ubuntu 直接安装课程工具链。命令与 Linux 同学完全一致，只是少了一层容器隔离。

## 第 1 步：安装 WSL2 + Ubuntu

以管理员身份打开 PowerShell：

```powershell
wsl --install
```

重启电脑后，按提示创建 Ubuntu 用户名和密码。

## 第 2 步：安装课程工具链

在 Ubuntu 终端内执行：

```bash
sudo apt update
sudo apt install -y build-essential gfortran libomp-dev openmpi-bin libopenmpi-dev make cmake git libgtest-dev doxygen python3 python3-numpy python3-matplotlib python3-mpi4py
```

## 第 3 步：获取仓库并验证

```bash
git clone git@gitee.com:wenyu-lei/parallel-and-distributed-computing.git
cd parallel-and-distributed-computing
gcc -fopenmp --version | head -1
mpirun --version | head -1
```

> 提示：WSL2 中的文件可以从 Windows 资源管理器通过 `\\wsl$\Ubuntu\home\<用户名>` 访问；也可以用 VS Code 的 "WSL" 扩展直接在 Ubuntu 中编辑代码。
