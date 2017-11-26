# Java概述

## 历史
起源于sun公司后被Oracel公司合并
java.sun.com---oracel.com

Java三大平台
- Java SE
- Java EE
- Java ME

## 相关词

1.**JVM** Java Virtual Meachine
JVM Java虚拟机，定义了Java程序运行的环境，如指令集，寄存器集......虚拟cpu与内存结构等  
JVM 给Java程序带来了很多优点，如安全性，跨平台，自动垃圾回收  

2.**JRE** Java Runtime Environment
当不作java程序开发，而仅仅是运行java程序时，下载安装JRE即可
3.**JDK** Java Development Kit
java开发者必备
```
三者的关系大致是这样的：  
JRE = JVM + API(Lib)  
JDK = JRE + Tools(Complier,Debugger...)
```
## 核心机制
- JVM
- Code Security
- Garbage Collection

## 特点
Java语言与C++类似，语法更为简单
- OOP较纯粹于C++
- 平台无关性
- 安全稳定
- 支持多线程（来源于JVM）
- 丰富的类库
```
Java与C++的一些区别:
*** 无直接指针操作
*** 自动内存管理,无delete
*** 数据类型长度固定(JVM)
*** 不用头文件
*** 不包含结构和联合
*** 不支持宏
*** 不用多重继承
*** 无类外全局变量
*** 无 goto
```
## 编译与运行机制
```
                                             |-----JVM for Dos
source.java---source.class（字节码bytecode，用于JVM） |------JVM for Win
                                             |-----JVM for UNIX
```
## Tools
- javac---------complier
- java----------
- jar-----------
- javaw---------
- javadoc-------

## 开发环境
(1) 直接使用JDK   
(2) 文本工具 + 调用JDK   
(3) IDE,如eclipe,NetBeans   
(4) 自己配置文本编辑器   

