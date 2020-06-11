---
title: C++ 强制转换类型
date: 2020-06-03 14:52:00
categories:
- C
- CPP
tags:
- C
- CPP
---

# 四类强制转换类型函数

## `const_cast`

- 常量指针与非常量指针之间的转换
- 常量引用与非常量引用之间的转换

```c++
    int a_int;
    a_int = 5;
    const int& b_int = a_int;
    int& c_int = const_cast<int&>(b_int);
    c_int = 6;
    cout<<"a: "<<a_int<<endl;               // 6

    int a_int = 5;
    const int& b_int = a_int;
    int& c_int = const_cast<int&>(b_int);
    c_int = 6;
    cout<<"a: "<<a_int<<endl;               // 6
```

## `static_cast`

- 类层次结构中基类和派生类之间的指针或引用的转换。`up_cast` 是安全的，`down_cast` 是不安全的
- 基本数据类型之间的转换，如：int 与 char等；
- > c++ primer: c++ 的任何隐式转换都是通过 `static_cast` 实现的

```c++
    A* a = new A(23, "wanncy");
    base* bs = static_cast<base*> (a);
    cout<<bs->getName()<<endl;
```

## `dynamic_cast`


## `reinterpret_cast`

## 参考

- [c++四种强制类型转换](https://blog.csdn.net/ydar95/article/details/69822540)