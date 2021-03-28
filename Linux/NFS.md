---
title: NFS(Network File System)
date: 2021-03-28 19:34:00
categories:
- Linux
tags:
- Linux
- NFS
---

# NFS(Network File System)

## 前述

>NFS或网络文件系统是一种分布式文件系统协议，最初是由Sun Microsystems构建的。通过NFS，您可以允许系统通过网络与其他人共享目录和文件。
>
> NFS在客户端 - 服务器环境中运行，其中服务器负责管理客户端的身份验证，授权和管理，以及特定文件系统内共享的所有数据。授权后，任意数量的客户端都可以访问共享数据，就好像它们存在于其内部存储中一样。在Ubuntu系统上设置NFS服务器非常简单。

## 配置

### 环境

- ubuntu 18.04

### 服务器端

1. 安装NFS服务器

    `sudo apt install nfs-kernel-server`

2. 创建导出目录，并更改权限
    
    `sudo chown nobody:nogroup ./share`

    `sudo chmod 777 ./share`
3. 通过NFS导出文件为客户端分配访问权限

    `sudo vim /etc/exports`

    参数的含义：
    - rw 可读写，ro 仅读
    - sync 修改同步到存储中，async 修改先同步内存，不立即同步到磁盘
    - all_squash 客户机上的任何用户访问该共享目录都映射为匿名用户
    - no_root_squash 客户机以 root 访问该文件时，不映射root用户，root_squash 客户机以 root 访问该文件时，映射为匿名用户
    - anonuid 将客户机上的用户访问映射为本机指定 **uid** 的用户
    - anongid 将客户机上的用户访问映射为本机指定 **gid** 的用户
4. 导出共享目录

    `sudo exportfs -a` 这一步会将 `/etc/exports` 中的 list 全部导出

    `sudo systemctl restart nfs-kernel-server`
5. 设置防火墙

### 客户机端

1. 安装NFS Common

    `sudo apt install nfs-common`

2. 创建目录并进行挂载

    `sudo mount -t nfs xx.xx.xx.xx:/home/share ./share`


### Tips

- `showmount -e <nfs server name>` 检查对应的NFS server上的共享目录
- 修改 `/etc/fstab` 进行自动挂载
- 为了使 NFS 服务端共享文件夹可以被客户端用户拥有正常的权限访问，可以通过设置服务端和客户端用户具有相同的 `uid` 和 `gid` 即可

    ```bash
    usermod -u xxx newsgrid
    groupmod -g xxx newsgrid
    ```
    
### 参考

- https://blog.csdn.net/weicao1990/article/details/90137680