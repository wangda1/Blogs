---
title: Heap 内存分配策略
date: 2018-05-09 00:22:00
categories:
- CTF
- Heap_Stack
tags:
- CTF
- Heap_Stack
---

# 详细摘录一下heap内存的分配策略

*应当好好阅读 glic 中关于 ptmalloc 的源码*

- <font color="#7600D8" size="4">根据用户 malloc 的 size 计算实际要分配 size</font>
- <font color="#7600D8" size="4"><br></font>
- <font color="#7600D8" size="4">当</font> <font color="#FF0000" size="4"><b>size < max_fast</b></font><font color="#7600D8" size="4">（默认是64B）在</font> <font color="#FF0000" size="4"><b>fast bins</b></font><font color="#7600D8" size="4">中取</font>
- <font color="#7600D8" size="4"><br></font>
- <font size="4"><font color="#7600D8">当 size > max_fast 或 在fast bins中没找到，在</font> <b><font color="#FF0000">small bins</font></b> <font color="#7600D8">（< 512B）找</font></font>
- <font color="#7600D8" size="4"><br></font>
- <font size="4"><font color="#7600D8">当 不满足 small bins的条件（fast bins和small bins均为精确查找），</font><b><font color="#FF0000">开始合并 fast bins（相邻的合并）连接到 unsorted bins</font></b><font color="#7600D8">，查找，若不满足，则</font><font color="#FF0000"><b>将 unsorted bins归类到 small bins或 large bins</b></font></font>
- <font color="#7600D8" size="4"><br></font>
- <font size="4"><font color="#7600D8">（注意，此时</font> <b><font color="#FF0000">all bins only small bins and large bins left</font></b><font color="#7600D8">）</font></font>
- <font color="#7600D8" size="4"><br></font>
- <font size="4"><font color="#7600D8">在</font> <b><font color="#FF0000">large bins</font></b><font color="#7600D8">中“smallest-first,best-fit”寻找分配，剩余link to the bins</font></font>
- <font color="#7600D8" size="4"><br></font>
- <font color="#7600D8" size="4">above is not fit.OK, go to the top chunk</font>
- <font color="#7600D8" size="4"><br></font>
- <font size="4"><font color="#7600D8">Top Chunk也不满足时，开始大招--</font><i><font color="#41AD1C">（</font></i><i><font color="#41AD1C">你到底是不是第一次调用？为什么都满足不了你）</font></i></font>
- <font color="#41AD1C" size="4">若你确实需要很多 >= mmap()阈值---syscall：1. main arena :调用 sbrk()增加 top chunk；2. thread arena：调用 mmap()增加一个 sub-heap </font>
- <font color="#41AD1C" size="4">若你是第一次调用 =>进行一系列初始化工作</font>