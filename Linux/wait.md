---
title: wait 使用
date: 2021-04-13 10:36:00
categories:
- Linux
tags:
- Linux
---

# wait command 使用

## `wait`

`wait [作业指示/进程号]` 等待作业号/进程号代表的进程退出，返回最后一个作业/进程的退出状态；Shell 中使用 `wait` 相当于多线程同步 

-  常和 `&` 搭配实现多线程的同步

栗子：
```bash
#!/bin/bash
for ((i=0;i<5;i++))
do
sleep 3;echo a
done

#运行需要15秒。


#!/bin/bash
for ((i=0;i<5;i++))
do
{
sleep 3;echo a
} &
done
wait

#打开5个子进程并行，运行只需要3秒。
```

## Refer

- [shell中wait命令详解](https://www.cnblogs.com/klb561/p/10740995.html)