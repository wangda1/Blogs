---
title: README
date: 2019-11-08 19:09:36
categories:
- Linux
- Network_Programming
tags:
- Linux
- Network_Programming
---

# 网络编程  

想以 UDPspeeder 这个udp加速项目为例真正地学习一下网络编程，去知乎上搜索了一下技术路线：
```
1.先看 图解tcp/ip 抓重点 。理解面向连接，无连接，tcp粘包，udp有界等
2.然后看 linux/unix系统编程手册 socket几章，号称超越apue的好书。这几章将socket,select,poll,epoll讲的很到位。理解select，poll的原理，大并发为啥epoll有优势，epoll的水平触发和边缘触发区别，如何解决边缘触发饿死问题等等。
3.看 tornado源码，这时候看起来应该比较轻松。比如tornado中用pipe做waker，上本书都有讲解。
4.阅读 effective tcp/ip ...
5.慢慢读 tcp/ip详解卷一和unix网络编程为啥最经典的书最后推荐，主要是让大家刚开始不要太纠结细节，unp实在太厚了，会吓死自己的。当能力够了再回头，才有共鸣，才有大收获。

作者：罗伊
链接：https://www.zhihu.com/question/29380313/answer/55937044
来源：知乎  
```

## 学习链接  
- [中科大linux socket 网络编程]http://staff.ustc.edu.cn/~mengning/np/linux_socket/new_page_36.htm

加油吧！
