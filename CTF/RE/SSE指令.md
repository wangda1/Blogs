---
title: SSE指令
date: 2018-05-03 20:22:00
categories:
- CTF
- RE
tags:
- CTF
- RE
---

# SSE指令

*https://blog.csdn.net/sunshine1314/article/details/1240641*

* * *

<br>SSE(Streaming SIMD Extensions)<br>
SIMD（单指令多数据）

SISD（单指令单数据）

对于指令仅能执行一次运算的cpu就是SISD处理器

一条指令可以同时作用于几个数据流的技术就是SIMD

- 多媒体指令集（主要用于图形处理：3D显示，音频处理等大量数据的处理）
- MMX---SSE
- MMX 仅能在整数上支持SIMD，可同时对2个32位数据进行操作
- SSE   可以在浮点数据上支持SIMD，可同时对4个32位浮点数据进行操作
- SSE新增了8个128位寄存器 mm0--mm7
- SSE指令集包括了70条指令：50条 SIMD指令（浮点）；12条 MMX（整数）；8条优化内存连续数据块传输指令
- MMX利用的寄存器是cpu中浮点运算的寄存器 mm0--mm7