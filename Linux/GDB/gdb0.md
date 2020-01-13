---
title: GDB 调试
date: 2019-11-08 19:09:36
categories:
- Linux
- GDB
tags:
- Linux
- GDB
---

# GDB常用命令

## 调试的运行和终结

- `n` 单步运行
- `c` 继续运行

## 断点的设置与清除

- `info b` 查看断点设置情况
- `b linenum_xxx` 设置断点
- `b/break filename_xxx.cpp:linenum_xxx thread all` 所有线程都在　filename.cpp 的　linenum　行设置断点

## 变量的查看

- `p value` 可以查看当前 value 对应的值
- `p &value`　可以查看当前 value 对应的地址
- `watch value` 对　value 的值进行监控，每当　value 的值发生变化则停止在对应的位置

## 内存的查看

`x number_xxx format_xxx unit_xxx addr_xxx` 以　format_xxx　格式显示　number_xxx　个以　unit_xxx　为单位的数据

- `number_xxx` 显示的内存单元数目
- `format_xxx` 显示格式：s-- 以字符串形式，i--以指令形式，u--16进制显示无符号整型
d-- 以十进制形式，f--以浮点格式形式，c--以字符格式形式；
- `unit_xxx` 内存单元的字节数：默认为　４　字节，b--单字节，h--双字节，w--四字节，g--八字节
- `addr_xxx` 内存的初始地址

## 线程的查看与切换

- `info threads` 显示当前所有的线程
- `thread thread_id_xxx` 切换线程
- `set scheduler-locking off|on|step` 在调式某一个线程时，其他线程是否执行。off，不锁定任何线程，默认值。on，锁定其他线程，只有当前线程执行。step，在step（单步）时，只有被调试线程运行。
- `set non-stop on/off` 当调式一个线程时，其他线程是否运行。
- `set pagination on/off` 在使用backtrace时，在分页时是否停止。
- `set target-async on/ff` 同步和异步。同步，gdb在输出提示符之前等待程序报告一些线程已经终止的信息。而异步的则是直接返回。

