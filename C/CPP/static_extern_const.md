---
title: static_extern_const
date: 2019-11-08 19:09:35
categories:
- C
- CPP
tags:
- C
- CPP
---

# static extern const

## static

静态，声明后变量的存储区域位于静态存储区

- **静态局部变量**：变量声明后位于静态存储区，但作用域仍限定在函数内部，即**不能被其他函数访问**
- **静态全局变量**：全局变量已经是静态的为什么还有static呢？作用在于限定作用域为本文件内部，即使其他文件 extern 也不能被访问到

## extern

引用，引用位于其它地方的声明，函数，变量等
如多个文件，一个文件中全局 int a;另一个文件中可以 extern int a;告诉编译器到其他文件中查找 a 的定义；

## const

这家伙用处比较大，容我一一道来 
**用const即意味着此对象不能够被改变**

### 常对象成员

**声明**

1. 类名 const 对象名: Student const stu1;  
2. const 类名 对象名: const Student stu1;  

### 性质

- 常对象的数据成员全部是**常数据成员**     
*如何初始化呢?*   构造函数的参数初始化表方式，不二法门!  
- 成员函数可不是常成员函数了，性质不变，但权限变了，**非常成员函数不得访问常对象数据，常成员函数能够访问不得修改!**     
*如何声明常成员函数呢？*   void get_time() const; 函数后加一个**const**
- 常成员函数不能调用另一个非 const 成员函数，即使此函数不修改数据，编译不通过

### 总结

![const keyword](./static_extern_const/const.png)
