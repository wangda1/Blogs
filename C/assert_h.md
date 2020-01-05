---
title: assert_h
date: 2019-11-08 19:09:35
categories:
- C
tags:
- C
---

# assert

这是一个断言语句，常用来过滤条件与检测错误信息

原型定义：
```void assert(int expression)```

用法示例：
```
#include <iostream>
#include <cassert>

using namespace std;

int main()
{
    int i = 1;

    assert(i<0);

    return 0;
}
```
输出：  
`Assertion failed: i<0, file D:\codes\acm\Test\main.cpp, line 10`

常用来调试程序，当调试结束时，可以在 include <assert.h> 前加上 **#define NDEBUG** 来禁用函数，具体见原型声明，
或
```
#ifdef BOUNDS_CHECK
	assert( 0 <= i );
	assert( i < nRow );
#endif
```
来方便调试
