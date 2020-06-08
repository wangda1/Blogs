---
title: 关于 ASLR 机制
date: 2018-05-08 16:57:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# 关于ASLR机制

<font color="#7600D8" style="font-size: 19px;">ASLR(Address Space Layout Randomization)地址空间布局随机化</font>
<font color="#7600D8">分为3级：0,1,2</font>

- <font color="#7600D8"><span style="font-size: 19px;">0：没有随机化。</span></font>
- <font color="#7600D8"><span style="font-size: 19px;">1：保留的随机化。共享库，栈，mmap( )及VDSO将被随机化</span></font>
- <font color="#7600D8"><span style="font-size: 19px;">2：完全的随机化。在1的基础上，通过brk( )分配的内存也将随机化</span></font>