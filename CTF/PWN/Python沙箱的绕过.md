---
title: Python 沙箱绕过
date: 2018-05-02 12:54:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# Python沙箱的绕过

*在国赛中第一次见到这种sand box的题目，不过没做出来*

<font color="#7600D8">思路通常是这样的：</font>

- <font color="#7600D8"><i>一般常用的可执行命令的模块如:os,subprocess等会被禁掉</i></font>
- <font color="#7600D8"><i>选择built-in 函数来执行命令</i></font>
- <font color="#7600D8"><i>执行的同时也避免不了字符串的绕过</i></font>
- <font color="#7600D8"><i>字符串绕过方法：编码与拼接</i></font>

<font color="#7600D8" size="4"><i><br></i></font>

<font color="#FF0000" size="4"><i>参考：</i></font>https://blog.csdn.net/qq\_35078631/article/details/78504415