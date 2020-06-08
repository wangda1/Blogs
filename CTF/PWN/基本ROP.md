---
title: 基本 ROP
date: 2018-04-25 19:42:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# 基本ROP

- **<font color="#FF0000" style="font-size: 19px;">ret2text:</font> <font color="#7600D8" style="font-size: 19px;">针对于存在system("/bin/sh")</font>**
- **<font color="#7600D8" size="4">寻找到system("/bin/sh")的函数入口；</font>**
- <font color="#7600D8" size="4"><b>溢出到函数入口处拿shell</b></font>

<font color="#FF0000" size="4"><b><br></b></font>

- <font size="4"><b><font color="#FF0000">ret2shell:</font> <font color="#7600D8">针对于存在可执行段并且可读入指令</font></b></font>
- <font color="#7600D8" size="4"><b>存在可执行段如：.bss段</b></font>
- <font color="#7600D8" size="4"><b>存在输入及复制函数</b></font>
- <font color="#7600D8" size="4"><b>输入shellcode，并溢出至可执行段(.bss)拿shell</b></font>

<font color="#7600D8" size="4"><b><br></b></font>

- ** ****<font color="#FF0000">ret2sys:</font> <font color="#7600D8">这个针对面较广</font>**
- <font color="#7600D8" size="4"><b>条件：多个带有pop的gadget，int 80h（linux）</b></font>
- <font color="#7600D8" size="4"><b>找多个gadget来准备syscall条件</b></font>
- <font color="#7600D8" size="4"><b>准备数据满足gadget构造payload</b></font>
- <font color="#4DCE1D" size="4"><b>工具：ROPgadget找gadget的好工具</b></font>

<font color="#4DCE1D" size="4"><b><br></b></font>

<font color="#4DCE1D" size="4"><b>     </b></font>

<font color="#7600D8" size="4"><b><br></b></font>