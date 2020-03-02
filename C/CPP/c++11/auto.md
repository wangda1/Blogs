---
title: auto 关键字
date: 2020-03-02 22:48
categories:
- C
- CPP
- c++11
tags:
- C
- CPP
- c++11
---

# auto 关键字的使用

`auto` 关键字是 c++ 11 引入的自动推导关键字，主要用途有：

1. 声明变量时根据初始化表达式自动推断该变量的类型；
2. 声明函数时，函数返回值的占位符

`auto` 关键字适用于类型冗长复杂时，如：

```c++
std::vector<int> vect;
for(auto it = vect.begin(); it != vect.end(); ++it)
{  //it的类型是std::vector<int>::iterator
    std::cin >> *it;
}
```

或者保存 lambda 表达式的变量声明：

```c++
auto ptr = [](double x){return x*x;};//类型为std::function<double(double)>函数对象`
```

# 参考

1. https://blog.csdn.net/xiaoquantouer/article/details/51647865