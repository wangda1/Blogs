---
title: 一步一步 ROP 之 x64篇 
date: 2018-04-30 12:10:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# 一步一步ROP之x64篇

<br>首先关于x86与x64的区别：<br>
- <font color="#FF0000">内存地址范围：不能超过</font><font color="#7600D8">0x0000 7fff ffff f000（64位内存布局中这个地址是栈顶地址，以下属于用户内存空间）</font><font color="#FF0000">，否则将抛出异常</font>
- <font color="#FF0000">传参方式：x86使用栈方式，x64优先使用</font><font color="#7600D8">RDI,RSI,RDX,RCX,R8,R9</font><font color="#FF0000">寄存器，然后才是栈</font>