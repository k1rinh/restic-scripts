# restic-scripts

### 如何使用

#### 1. 克隆仓库到本地

```shell
mkdir ~/.config
cd ~/.config
git clone https://github.com/k1rinh/restic-scripts.git restic
cd restic
```

#### 2. 修改仓库地址和密码

```shell
# cd ~/.config/restic
# 修改仓库地址
vim repository.txt
# 修改仓库密码
vim password.txt
```

```shell
# 初始化仓库，如果已经初始化则忽略
source ./env.sh
restic init
# 检查仓库
restic cat config
```

#### 3. 手动执行备份

这里以 Umami 为例，已经在仓库里了，在此基础上进行修改以使用。

```shell
cd umami
# 手动运行一次备份脚本
bash ./backup.sh
# 查看备份是否如预期
restic ls latest
```

#### 4. 创建计划任务

```shell
# 按需修改 Systemd Unit 文件
# 替换 service 文件中的 HealthChecks Ping 地址
sed -i 's|https://hc-ping.com/your-uuid-here|https://hc-ping.com/your-uuid-here2|g' restic-umami-backup.service
```

```shell
# 移动 Systemd Unit 文件
mkdir -p ~/.config/systemd/user
# 采用软链接而不是复制，方便统一管理
# cp restic-* ~/.config/systemd/user/
ln -sf ~/.config/restic/umami/restic-* ~/.config/systemd/user/
systemctl --user daemon-reload
# 手动运行一次
systemctl --user start restic-umami-backup.service
systemctl --user status restic-umami-backup.service
```

```shell
# 启动计时器
systemctl --user enable --now restic-umami-backup.timer
# 允许指定用户的用户级 systemd 实例在启动时自动运行（无需登录）
# 不然的话，必须得登录该用户才会运行这个计划任务
sudo loginctl enable-linger $USER
```
