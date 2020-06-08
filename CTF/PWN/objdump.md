---
title: objdump
date: 2018-05-02 12:54:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# objdump

*objdump是个神器，下面要攒一波儿它的用法*

- <font color="#7600D8" size="4"><i>objdump -R XXX  (Dynamic Relocation Records) 当然是可用于显示GOT表</i></font>
- <font color="#7600D8" size="4"><i>objdump -d -j .plt XXX 可用于显示 .plt 表了</i></font>
- <font color="#7600D8" size="4"><i>objdump -h 显示目标文件各个section的头部摘要信息</i></font>