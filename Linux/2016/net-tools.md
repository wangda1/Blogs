---
title: net-tools
date: 2019-11-08 19:09:36
categories:
- Linux
- 2016
tags:
- Linux
- 2016
---

## net-tools网管工具集  

接上篇，当具体分析连接对应的端口号与查看相应的进程号与名字(PID与program name)时  

> - netstat -apn  win也可以使用这个命令哦  

嗯？cannot find？惊呆了   
google一下发现没安装工具集   
> - yum install net-tools  

再次使用果然可以了，里面会显示开放的所有端口，及对应的PID和文件所在位置，下面会展示出来所有的sockets  

> - netstat -apn | grep 80  可以具体地查找某个具体端口的开放情况   


## ps PID
**ps PID 也可以具体地查看某个进程对应的端口及一些详尽信息哦**  

