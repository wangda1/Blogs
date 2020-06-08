---
title: UAF & Double Free
date: 2018-05-08 15:14:00
categories:
- CTF
- Heap_Stack
tags:
- CTF
- Heap_Stack
---


# UAF & Double Free

- UAF( use after free)

<font color="#1C3387">          释放重用漏洞，具体导致原因是对释放的指针没有赋值为空，</font>

<font color="#7600D8"><br></font>

<font color="#7600D8"><br></font>

- <font color="#7600D8"><span style="font-size: 21px;">Double Free</span></font>
- <font color="#7600D8"><span style="font-size: 21px;"><a href="https://bbs.pediy.com/thread-225688.htm"><i>https://bbs.pediy.com/thread-225688.htm</i></a></span></font>
- <font color="#4F009A">通过这篇文章，好像有点明白Double Free的意思了：臆测一下Free的过程：</font>

1. <font size="4">检测是否为NULL，若为NULL则报错？否则进行释放操作</font>
2. <font size="4">检测是否满足合并条件（前向或者后向合并），若满足进行 unlink 操作</font>

<font size="4"><br></font>

- <font size="4"><font color="#E30000">漏洞利用点：</font></font>

1. <font size="4"><font color="#E30000">先申请2个小的（空间进行布局），释放，再申请一个大的（2个小的之和），释放满足 unlink 条件，偷梁换柱可写指针，进行WAA（任意地址写入）</font></font>
2. <font size="4"><font color="#E30000">利用 fastbin + 堆溢出 修改邻近 chunk 标志位，释放，达到 unlink</font></font>