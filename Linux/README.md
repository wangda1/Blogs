---
title: README
date: 2019-11-08 19:09:36
categories:
- Linux
tags:
- Linux
---

# Linux Tips

## `set` command

Linux `set` 命令用于设置 Shell，set 指令能设置所使用 shell 的执行方式，可依照不同的需求来设置

`set [+-abCdefhHklmnpPtuvx]`

```bash
-参数 表示设置某个参数  Enable
+参数 表示取消设置的参数 Disable
```

## 关于 `sh` 与 `./` 的区别

./ 需要script是可执行的，用到的解释器是第一行声明的 !/bin/bash, !/bin/sh

因此，当 script 中第一行是 `!/bin/bash` 时，使用

- `./xxx_script.sh` 是相当于使用 `/bin/bash` 解释器；
- `sh xxx_script.sh` 是相当于使用 `/bin/sh` 解释器；

两者对 shell 命令的解释是有区别的，比如上述中的 `set` 命令

## 查看当前登录的用户

`w/who`