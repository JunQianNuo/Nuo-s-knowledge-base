---
raw_title: Linux常用命令
subject: Linux常用命令
source: Linux常用命令.pdf
status: mineru解析
parser: mineru
---

lines。 head head。 tail tail。 less less。 more more。 cat concatenate。 tac tac（cat 反写）。 diff difference。 cmp compare。 echo echo。 printf print formatted。 tee tee。

find find。 locate locate。 which which。 whereis where is。 updatedb update database。basename base name。 dirname directory name。 tree tree。 stat status。 file file。 ln link。cp copy。 mv move。 rm remove。 mkdir make directory。 rmdir remove directory。 touchtouch。 pwd print working directory。 cd change directory。 ls list。

可以了。

现在生成最终回答。注意格式简洁。可以每类用无序列表，每项： 命令 ：英文全称/来源 —— 用法。示例中带说明。不要太多解释。

最后加注意事项： rm -rf 、 dd 、 mkfs 等危险；用 man 、 --help 、 tldr 查询。

开始编写最终。

下面按用途整理 Linux 常用命令。说明：很多命令是历史缩写，并非严格“英文全称”；有些来自作者名或习惯命名。

## 1. 文件与目录

ls ：list —— ls -alh 列出文件详细信息

cd ：change directory —— cd /etc 切换目录

pwd ：print working directory —— pwd 显示当前目录

mkdir ：make directory —— mkdir -p a/b 创建目录

rmdir ：remove directory —— rmdir empty\_dir 删除空目录

touch ：touch —— touch file.txt 创建空文件/更新时间

cp ：copy —— cp -r src dst 复制文件或目录

mv ：move —— mv old.txt new.txt 移动/重命名

rm ：remove —— rm -rf dir 删除文件或目录，慎用

ln ：link —— ln -s target link 创建软链接

find ：find —— find / -name "\*.log" 查找文件

locate ：locate —— locate nginx.conf 快速查找

which ：which —— which python 查看命令路径

whereis ：where is —— whereis ls 查看命令相关路径

tree ：tree —— tree -L 2 树状显示目录

stat ：status —— stat file 查看文件状态

file ：file —— file a.out 判断文件类型

basename ：base name —— basename /a/b.txt 取文件名

dirname ：directory name —— dirname /a/b.txt 取目录名

updatedb ：update database —— sudo updatedb 更新 locate 数据库

## 2. 文本查看与处理

cat ：concatenate —— cat file 查看/拼接文件

tac ：cat 反写 —— tac file 反向显示

less ：less —— less file 分页查看，可搜索

more ：more —— more file 分页查看

head ：head —— head -n 10 file 看前 10 行

tail ：tail —— tail -f file 实时看末尾

nl ：number lines —— nl file 加行号

wc ：word count —— wc -l file 统计行数/词数/字节

sort ：sort —— sort file 排序

uniq ：unique —— uniq -c 去重并计数

cut ：cut —— cut -d: -f1 /etc/passwd 按列截取

paste ：paste —— paste a.txt b.txt 按行合并

tr ：translate —— tr 'a-z' 'A-Z' 字符转换

sed ：stream editor —— sed 's/old/new/g' file 流式编辑

awk ：Aho, Weinberger, Kernighan —— awk '{print \$1}' file 文本处理

grep ：global regular expression print —— grep -rn "text" . 搜索文本

diff ：difference —— diff a b 比较文件差异

cmp ：compare —— cmp a b 比较二进制差异

echo ：echo —— echo "hello" 输出文本

printf ：print formatted —— printf "%s\n" hello 格式化输出

tee ：tee —— cmd | tee file 输出到屏幕并写文件

## 3. 权限与用户

chmod ：change mode —— chmod 755 file 修改权限

chown ：change owner —— chown user:group file 修改所有者

chgrp ：change group —— chgrp dev file 修改所属组

umask ：user file-creation mode mask —— umask 022 设置默认权限掩码

su ：substitute user —— su - root 切换用户

sudo ：superuser do —— sudo apt update 以管理员执行

passwd ：password —— passwd user 修改密码

useradd ：user add —— useradd -m tom 添加用户

usermod ：user modify —— usermod -aG sudo tom 修改用户

userdel ：user delete —— userdel -r tom 删除用户

groupadd ：group add —— groupadd dev 添加组

groupdel ：group delete —— groupdel dev 删除组

id ：identity —— id 查看 UID/GID

whoami ：who am I —— whoami 当前用户

who ：who —— who 查看登录用户

w ：who —— w 查看登录用户及活动

last ：last —— last 查看登录历史

groups ：groups —— groups 查看用户组

## 4. 进程与作业

ps ：process status —— ps aux 查看进程

top ：table of processes —— top 动态查看进程

htop ：htop —— htop 交互式进程查看

kill ：kill —— kill -9 PID 终止进程

killall ：kill all —— killall nginx 按名称终止

pkill ：process kill —— pkill -f java 按模式终止

pgrep ：process grep —— pgrep ssh 查找 PID

pidof ：process ID of —— pidof sshd 查 PID

jobs ：jobs —— jobs 查看后台作业

bg ：background —— bg %1 后台运行

fg ：foreground —— fg %1 前台运行

nohup ：no hang up —— nohup cmd & 退出终端不中断

nice ：nice —— nice -n 10 cmd 调整优先级

renice ：renice —— renice 5 -p PID 修改优先级

free ：free —— free -h 查看内存

uptime ：uptime —— uptime 查看运行时间/负载

watch ：watch —— watch -n 1 date 周期执行

screen ：screen —— screen -S name 会话保持

tmux ：terminal multiplexer —— tmux new -s name 终端复用

## 5.系统与磁盘

uname ：Unix name —— uname -a 系统信息

hostname ：host name —— hostname 主机名

date ：date —— date 日期时间

cal ：calendar —— cal 日历

df ：disk free —— df -h 磁盘空间

du ：disk usage —— du -sh \* 目录占用

mount ：mount —— mount /dev/sdb1 /mnt 挂载

umount ：unmount —— umount /mnt 卸载

fdisk ：fixed disk —— sudo fdisk -l 磁盘分区

lsblk ：list block devices —— lsblk 块设备

blkid ：block ID —— blkid 块设备 UUID

mkfs ：make filesystem —— mkfs.ext4 /dev/sdb1 格式化

fsck ：file system check —— fsck /dev/sdb1 文件系统检查

sync ：synchronize —— sync 刷写缓存

dmesg ：display message —— dmesg | tail 内核日志

lsof ：list open files —— lsof -i:80 查看打开文件/端口

lscpu ：list CPU —— lscpu CPU 信息

lsusb ：list USB —— lsusb USB 设备

lspci ：list PCI —— lspci PCI 设备

vmstat ：virtual memory statistics —— vmstat 1 虚拟内存统计

iostat ：input/output statistics —— iostat -x 1 IO 统计

sar ：system activity reporter —— sar -u 1 3 系统活动报告

## 6. 网络

ping ：Packet Internet Groper —— ping -c 4 baidu.com

ip ：Internet Protocol —— ip addr 查看 IP

ifconfig ：interface configuration —— ifconfig 查看网卡

netstat ：network statistics —— netstat -tunlp

ss ：socket statistics —— ss -tunlp

route ：route —— route -n 路由表

traceroute ：trace route —— traceroute baidu.com

tracepath ：trace path —— tracepath baidu.com

nslookup ：name server lookup —— nslookup baidu.com

dig ：Domain Information Groper —— dig baidu.com

host ：host —— host baidu.com

curl ：Client URL —— curl -I https://example.com

wget ：Web Get —— wget https://example.com/file

ssh ：Secure Shell —— ssh user@host

scp ：Secure Copy —— scp file user@host:/tmp

sftp ：SSH File Transfer Protocol —— sftp user@host

rsync ：remote synchronization —— rsync -av src/ user@host:/dst/

telnet ：teletype network —— telnet host 80

nc ：netcat —— nc -zv host 80

tcpdump ：TCP dump —— sudo tcpdump -i eth0 port 80

nmap ：Network Mapper —— nmap -sP 192.168.1.0/24

ftp ：File Transfer Protocol —— ftp host

## 7. 压缩与包管理

tar ：Tape Archive —— tar -czvf a.tar.gz dir 压缩； tar -xzvf a.tar.gz 解压

gzip ：GNU zip —— gzip file

gunzip ：GNU unzip —— gunzip file.gz

bzip2 ：bzip2 —— bzip2 file

bunzip2 ：bunzip2 —— bunzip2 file.bz2

xz ：xz —— xz file

unxz ：unxz —— unxz file.xz

zip ：zip —— zip -r a.zip dir

unzip ：unzip —— unzip a.zip

7z ：7-Zip —— 7z x a.7z

apt ：Advanced Package Tool —— sudo apt install nginx

apt-get ：Advanced Package Tool get —— sudo apt-get update

dpkg ：Debian package —— dpkg -i a.deb

yum ：Yellowdog Updater Modified —— sudo yum install nginx

dnf ：Dandified YUM —— sudo dnf install nginx

rpm ：Red Hat Package Manager —— rpm -ivh a.rpm

pacman ：package manager —— sudo pacman -S nginx

zypper ：Zypper package manager —— sudo zypper install nginx

snap ：snap —— sudo snap install code

flatpak ：flatpak —— flatpak install flathub app

pip ：Pip Installs Packages —— pip install requests

npm ：Node Package Manager —— npm install express

## 8.服务、计划与帮助

systemctl ：system control —— systemctl status nginx

service ：service —— service nginx restart

journalctl ：journal control —— journalctl -u nginx -f

crontab ：cron table —— crontab -e 编辑定时任务

at ：at —— at 10:00 一次性定时任务

reboot ：reboot —— sudo reboot

shutdown ：shutdown —— sudo shutdown -h now

poweroff ：power off —— sudo poweroff

halt ：halt —— sudo halt

man ：manual —— man ls

info ：info —— info ls

whatis ：what is —— whatis ls

apropos ：apropos —— apropos password

alias ：alias —— alias ll='ls -al

history ：history —— history

export ：export —— export PATH=\$PATH:/opt/bin

env ：environment —— env

source ：source —— source \~/.bashrc

exit ：exit —— exit

clear ：clear —— clear

seq ：sequence —— seq 1 10

sleep ：sleep —— sleep 2

yes ：yes —— yes hello

## 学习建议查用法： man 命令 、 命令 --help 、 tldr 命令危险命令慎用： rm -rf 、 dd 、 mkfs 、 fdisk 、 chmod -R 777

大多数命令支持 -h / --help 查看参数。

和 DeepSeek 继续聊