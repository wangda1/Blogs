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

**auto的类型推导实际上在编译过程中由编译器自动推导完成，实际上是个语法糖，但是很实用！**

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

# `auto` 与 `decltype` 区别

`auto` 进行编译器自动类型推导的时候需要指定初始值，但使用 `decltype` 可以进行不进行初始化进行类型声明。

```c++
int add(int x,int y){
    return x+y;
}
int main(){
    double i=0;
    decltype(i) a; // double
    decltype(add()) b; //int 注意括号。不带括号就是函数指针了。
}
```

# 参考

1. https://blog.csdn.net/xiaoquantouer/article/details/51647865