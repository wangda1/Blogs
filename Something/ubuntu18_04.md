---
title: ubuntu 18.04 简单配置指南
date: 2020-09-20 22:28:00
categories:
- Something
tags:
- Something
---

# ubuntu 18.04 简单配置

ubuntu 18.04 系统代号：bionic

## 系统安装

- 从 https://ubuntu.com/download/alternative-downloads 下载选择的系统版本（这里我选择的是 18.04）
- 使用 UtralISO 找一个空U盘制作启动盘
- 重启电脑，进入BIOS，更改启动项，安装即可

## 桌面环境

ubuntu 的桌面环境大概有：KDE，gnome，Unity三种，ubuntu 18.04 默认桌面环境为 gnome

查看当前桌面环境：`echo $XDG_CURRENT_DESKTOP`

### 工具安装

```shell
sudo apt-get update
sudo apt-get install gnome-tweak-tool   # tweak 用来管理主题和插件
sudo apt-get install gnome-shell-extensions
sudo apt-get install gnome-shell-extension-dashtodock   # dashtodock 用来管理dock
```

### 主题安装

这里参考：[ubuntu18.04美化总结](https://www.jianshu.com/p/6ef16e3b0a3e) 选用 Sierra Gtk Theme 主题进行安装

```shell
sudo add-apt-repository ppa:dyatlov-igor/sierra-theme
sudo apt update
sudo apt install sierra-gtk-theme       # point releases
```

*这里 `add-apt-repository` 都会在/etc/apt/sources.list.d/下创建一个.list文件，可以通过删除该文件来移除对应仓库的公钥链接ppa* 

### 桌面环境管理

在 tweaks 工具中，可对整个桌面环境的组件进行管理，如：主题，字体，键盘，窗口，扩展组件等

![tweaks_tool](./ubuntu18_04/tweaks_screen_capiture.png)

注：Shell 的更改需要打开 Extensions -> User Themes 开关

我的设置主要参考：[ubuntu18.04美化总结](https://www.jianshu.com/p/6ef16e3b0a3e)

## 输入法

- 安装 fcitx 输入框架（ubuntu默认的是ibus，比较难用）
`sudo apt install fcitx`
- 下载安装 搜狗输入法
- 在系统设置（右上角的电源选项中）-> Region & language -> 安装中文语言-> 将输入法系统设置为 fcitx
![language support](./ubuntu18_04/language_support.png)

- 重启电脑，选择屏幕窗口上方的 fcitx 的键盘图标，添加 Sogou Pin 输入法即可
- 注：添加搜狗输入法时需要取消 `only current language` 选项，搜索 `sogou` 而不是 `sougou` ！！！

## 其它常用软件

- VLC media player 多媒体播放器
- sublime text 编辑器
- Chrome 浏览器
- VS code
- tilix 终端模拟器
- thunderbird 邮箱客户端
- ...

### 设置桌面启动器

ubuntu 的 dash home 中的每个图标都对应 `/usr/share/applications` 中的一个 .desktop 的配置文件

只有在 dash 中的可执行程序才可以在 dock 中 add to favorites

- `dpkg -i xxx.deb` 的方式安装，会自动建立桌面启动器对应的 .desktop 文件
- 使用 tar 包解压的方式，直接运行可执行文件，需自己手动设置启动器

```
sudo vim /usr/share/applications/xxx.desktop

# 复制以下内容，修改对应的 exec 和 icon 选项

[Desktop Entry]

Version=1.0

Name=eclipse

Exec=/PATH/TO/EXEC/FILE

Termina=false

Icon=/PATH/TO/ICON

Type=Application

Categories=Development
```

或许还需要重启下 Gnome `alt` + `F2`，`r` + `Enter`

### 磁盘挂载

一般会选择将一块大的磁盘挂载到 `/home` 目录

1. 先在其他目录下新建一个备份目录，将要挂载的盘挂载到该新建目录上
   `mount /dev/sdb1 /new`
2. 将现有目录的所有文件（包含隐含文件）复制到新建目录：
   `cp -r /home/. /new` 
   （注：删除一个目录下的所有文件，包括隐含文件：先删除非隐藏文件： rm -rf /home/\*；再删除隐藏文件： rm -rf /home/.*）
3. 将 /dev/sdb1 与 /new 目录取消挂载，可能出现 target busy 的情况
   `umount /dev/sdb1 -fl`
4. 将 /dev/sdb1 挂载到 /home
   `mount /dev/sdb1 /home`
5. 将挂载命令写到 `\etc\fstab`
   `/dev/sdb1   /home   ext4    defaults    0   0`\

### 管理磁盘分区

```bash
fdisk       #  磁盘相关操作
df          #  系统分区挂载信息，查看已使用磁盘信息
df -h
du          #  系统分区挂载信息，查看空闲磁盘信息
du -s /* | sort -nr  #  查看哪个目录占用的空间大
du -s /home/* | sort -nr   #  逐层查找哪个目录占用的空间大

mount       #  挂载分区
umount      #  卸载分区
mkfs.ext4   #  格式化分区
```

#### 新增/删除分区

- 新增分区

    `fdisk /dev/sdb` -> `n` （新建分区） -> `p/e`（主分区/扩展分区） -> `_enter_` （柱面起始值，回车确认） -> `_enter_`（分区大小） -> `w` （写入磁盘分区表）

- 格式化分区

    `mkfs.ext4  /dev/sdb1`  # 格式化成 ext4 文件系统

- 删除分区

   删除之前，应当先使用 `umount` 卸载对应的分区
    `fdisk /dev/sdb` -> `d`（删除分区） -> `_num_` （删除的分区号） -> `w`（写入磁盘分区表）
- 格式化分区

   `mkfs.ext4 /dev/sdb`

### systemd 与 `systemctl`

`systemctl` 的两大主要功能：
- 控制 systemd 系统
- 管理系统上运行的服务

### `systemd` 与 1 号进程

![PID_1](./ubuntu18_04/init_pid_1.png)

可以看到 systemd 是 `/sbin/init` 的软链接，因此是 PID=1 的 init 进程

### 常用命令

- `systemctl list-units`， 查询所有的 units（aka daemons 或在 win 中 services）就是后台运行的守护进程
   - `systemctl list-units | grep service`
- `systemctl status ssh.service` 查看
   ![status service](./ubuntu18_04/status_service.png)
   - Loaded: enabled，开启自启动
      - `systemctl enable/disable ssh.service`
   - Active: active(running)，是否正在运行
      - `systemctl start/restart/stop ssh.service`
   - 下方的 log 是启动运行的 log
- `systemctl reboot/poweroff/suspend` 开/关机
- `journalctl` 查看 units 日志
   - `journalctl -b` 查看自 boot 以来的启动日志

参考：https://www.cnblogs.com/sparkdev/p/8472711.html

## FAQ

### 快捷键不work

键盘快捷键的设置在 settings -> Devices -> Keyboard 中，可以在这里更改已有的快捷键或新建快捷键选项

### 出现图形界面循环登录

问题排查，通过 tty 登录

```shell
ctrl+alt+F1 进入 tty
#输入账户名和密码登入
startx  # 启动 Xserver
ls -l ~/.Xauthority # 查看 Xauthority 对应的权限信息是否为需要登录的账户
```