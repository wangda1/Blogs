---
title: RELRO
date: 2018-05-11 10:42:00
categories:
- CTF
- Heap_Stack
tags:
- CTF
- Heap_Stack
---


# RELRO

- <font color="#7600D8">设置符号重定向表格为只读或在程序启动时就解析并绑定所有动态符号，从而减少对GOT表（Global Offset Table）攻击。</font>
- <font color="#FF0000">当RELRO为"Partial RELRO"，说明对GOT表具有读写权限</font>