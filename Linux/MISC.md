---
title: Linux 命令杂谈
date: 2020-03-22 16:22:00
categories:
- Linux
tags:
- Linux
---

# Linux 命令杂谈

## 进程查看命令

- `ps -aux` 与 `ps aux` 与 `ps -ef`

输出都是一样的，是当前终端机下的所有进程，至于几个的主要区别：
`ps -aux` 等价于 `ps aux`，但可能会截断 COMMAND 列的输出，不适用于 `grep` 搭配，而 `ps -ef` 不存在这种情况，可与 `grep` 进行搭配使用。

## `nohup xxx &`

后台不挂断运行

- `nohup` （no hang up）程序不挂断的运行，即无论终端是否断开，都会一直运行，但没有后台运行的功能；
- `&` 后台运行，但没有不可挂断执行的功能；

因此常将两者结合使用用于不可挂断的后台执行。

如何查看？

如果终端没有关闭，`jobs` 可以查看当前终端下的进程

## 查看内核及操作系统版本

### 查看内核版本

- `uname -a`
- `uname -r`

关于 Linux 内核版本号的格式：

major.minor.patch-build.desc

### 查看操作系统版本

- `cat /proc/version`
- `cat /etc/issue`
- `lsb_release -a` 适用于 Ubuntu/Debian

## `wget` 下载工具

- `wget -b xxx_url` 下载 `xxx_url` 对应的内容并后台下载