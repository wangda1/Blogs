---
title: ubuntu 显示管理器和桌面环境
date: 2021-01-15 16:56:00
categories:
- Something
tags:
- Something
---

# ubuntu显示管理器和桌面环境

## 显示管理器（Display Managers）

显示管理器（Display Manager，DM），通常是登录界面的代名词，为Linux发行版提供登录功能，控制用户会话并管理用户认证。显示管理器在验证用户名及密码后会立即启动显示服务器并加载桌面环境。

显示管理器是一个独立的程序并不是桌面环境的一部分，可以与桌面环境配合使用

一些流行的显示管理器有：
- GDM（GNOME Display Manager）：GNOME的首选
- SDDM（Simple Desktop Display Manager）：KDE的首选
- LightDM：Ubuntu为 Unity桌面开发

## 桌面环境（Desktop Environments）

桌面环境是一个组件的组合体，提供常见的图形用户界面Graphical User Interface（GUI）元素组件。大多数桌面环境都有一套集成的应用程序和实用程序，如：文本编辑器、桌面搜索、应用程序菜单等

一些流行的桌面环境：
- GNOME 
- Xfce
- KDE
- LXDE

## 显示服务器（Display Servers）

> Display Server is the basic component of GUI which sits between the graphical interface and the kernel. Its primary task is to coordinate the input and output of its clients (programs and applications running GUI interface) to and from the rest of the OS, the hardware, and each other. It communicates with its clients over the display server protocol which can be network-transparent and network capable. Commonly known display server communications protocols include X11, Wayland, Mir, etc.
X11 is the protocol implemented by X Windows System while Wayland is the protocol used by Wayland Compositor. In simple terms, X Windows System and Wayland determine how your program's display will appear depending on your actions. These actions include clicking on a checkbox, moving the windows, clicking a button, etc. The X Window System is a client/server network protocol that's been put into use for a while now. X.Org Server is the free and open source implementation of the display server for the X Window System stewarded by the X.Org Foundation. Wayland is a computer protocol that specifies the communication between a display server (called a Wayland compositor) and its clients.

一些流行的显示服务器：
- Xorg
- Wayland

## Q&A

1. ubuntu登录界面（显示管理器的一部分）出现 `ubuntu`，`ubuntu on wayland` 两种选项的含义：

what this means, seeing these 2 options, is that you have one desktop environment, namely Ubuntu, and 2 display servers installed, and you can choose whichever you want; so which one should you choose?

Xorg has been around a long time, so it is likely that all linux programs work with it; so if you don't want to have things not working anymore, choose Xorg;

Wayland is new, and some programs do not work with it, such as gparted, or screen recorders, etc; one question here even noted that Wayland turns off your nvidia, causing the laptop to heat up;

to see which display server you are using, in a terminal/at a command prompt try this:

`echo $XDG_SESSION_TYPE`

so, if you are trying Wayland and things don't work, log out, click on the icon on the login screen and choose Xorg then log back in.

Also if you have more than one display manager installed, for example you have gdm3 and lightdm, to check which one you are using, type at a terminal command prompt:

`cat /etc/X11/default-display-manager`

and to switch between them type

`sudo dpkg-reconfigure lightdm`

or

`sudo dpkg-reconfigure gdm3`

A text window appears where you can use the arrow keys to select one of the installed display managers and press enter.

It is possible to install other desktop environments as well, such as one or more of these or others, and then they will also appear in the list of desktop environments which you can choose from, before logging in:

```
sudo apt-get install xfce4
sudo apt-get install kde-plasma-desktop
sudo apt-get install lxde
sudo apt-get install openbox
sudo apt-get install fluxbox
```
Then the desktop environments list to choose from before login might look like this:
```
Fluxbox
LXDE
Openbox
Plasma
Ubuntu
Ubuntu on Wayland
Xfce Session
```

## Linux 中的两套网络连接管理方案

- `/etc/network/interfaces（/etc/init.d/networking）`
- `Network-Manager`

两套方案是冲突的
- 第一个适合于没有 X 的环境，如服务器等网络连接不发生变化的场合
- 第二个适合于有桌面的环境，如笔记本等网络环境经常变化的场合

他们两个为了避免冲突，又能共享配置，就有了下面的解决方案：

1. 当Network-Manager发现/etc/network/interfaces被改动的时候，则关闭自己（显示为未托管），除非managed设置成真。
2. 当managed设置成真时，/etc/network/interfaces，则不生效。

## 参考

- https://zhuanlan.zhihu.com/p/272740410
- https://www.secjuice.com/wayland-vs-xorg/
- https://askubuntu.com/questions/1138155/ubuntu-on-wayland
