---
title: namespace
date: 2019-11-08 19:09:35
categories:
- C
- CPP
tags:
- C
- CPP
---

# namespace

关于命名空间的使用

- 概念

`命名空间，所谓命名空间，实际上就是一个由程序设计者命名的内存区域`

- 背景

在不同的头文件中包含有相同的函数名或者类名时，同时包含两个头文件，预编译是会出现编译错误，歧义

- 解决方式

1.别名

`namespace TV = Television`

2.using 命名空间成员名

`using std::cout`

3.using namespace 命名空间名

`using namespace std`  但这种方式在有很多命名空间时会带来麻烦

4.常用方式

命名空间较少或者类名与函数名较少时，常用 using namespace 的方式  
命名空间较多的时候常用一个头文件把 需要用到的类或函数包含在内  using xx::xx,using xx::yy,using yy::yy 


- 备注

1.当在mian函数中全局声明的变量，表面上不属于任何命名空间，实则属于隐含的 全局空间  
2.在命名空间中不能包含预处理   
3.命名空间可以嵌套  


