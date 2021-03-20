---
title: LVM(Logical Volume Manager)逻辑卷管理
date: 2021-03-20 16:22:00
categories:
- Linux
tags:
- Linux
- LVM
---

# LVM(Logical Volume Manager)逻辑卷管理

## LVM 出现的动机

传统磁盘管理：当分区大小不够用时无法扩展其大小，只能通过添加磁盘，创建新的分区来扩展空间，新添加进来的磁盘作为独立的文件系统存在，原有的文件系统并没有得到扩充，上层应用很多时候只能访问一个文件系统，因此只能让现有的磁盘下线，换上新的磁盘后，再将原来的数据导入。

## LVM 逻辑卷管理

LVM(Logical Volume Manager)逻辑卷管理通过将底层物理硬盘封装起来，以逻辑卷的形式表现给上层系统，逻辑卷的大小可以动态调整，而且不会丢失现有的数据。新加入的硬盘也不会改变现有的上层的逻辑卷。作为一种动态磁盘管理机制，逻辑卷技术大大提高了磁盘管理的灵活性。

## LVM 的分层组织结构

- PV(Physical Volume)
- PE(Physical Extend)
- VG(Volume Group)
- LV(Logical Volume)

![LVM_ARCH](./LVM/lvm_arch.png)

![LVM_ARCH](./LVM/lvm2.png)

## LVM 的管理命令

### 创建 LV（Logical Volume）

![create_lv](./LVM/create_lvm.png)

### 删除 LV（Logical Volume）

![delete_lv](./LVM/delete_lvm.png)

### 查看 LV

![display_lv](./LVM/display_lvm.png)

### 扩展 LV

扩展从下往上扩展，分别为：PV -> VG -> LV

![extend_vg](./LVM/extend_vg.png)

![extend_lvm](./LVM/extend_lvm.png)

### 缩小 LV

缩小从上往下缩小，分别为：LV -> VG -> PV

![zoom_out](./LVM/zoom_out.png)

![zoom_out_vg](./LVM/zoom_out_vg.png)

## tips 

除了 `fdisk -l`，使用 `lsblk` 是查看块设备的一个好方法，结果形式如下：

![lsblk](./LVM/lsblk_info.png)


## 参考

- Linux cast：https://www.youtube.com/watch?v=tSyXYRyZIW8&list=PLCJcQMZOafICYrx7zhFu_RWHRZqpB8fIW&index=21
- Linux 逻辑卷的创建、扩展、删减：https://blog.51cto.com/13805636/2154846