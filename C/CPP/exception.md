---
title: namespace
date: 2020-07-03 20:57:35
categories:
- C
- CPP
tags:
- C
- CPP
---

# 异常

C++ 对异常的处理可采用：

```c++
try
{

}
catch (int)
{

}
catch(myexception e)
{
    std::cout<<e.printError()<<std::endl;
}
catch(...)
{
    throw;
}
```

- 异常类可自定义，通过 `throw` 关键字抛出

## 栈解旋

从 `try` 开始到 `throw` 抛出异常之前，所有栈上的对象都会被释放，这个过程称为栈解旋。