---
title: C++ Singleton
date: 2020-02-10 09:06:00
categories:
- C
- CPP
- 设计模式
tags:
- C
- CPP
- 设计模式
---

# c++ 中的 单例模式

```c++

class CSingleton
{
private:
	CSingleton()   //构造函数是私有的
	{
	}
	CSingleton(const CSingleton &);
	CSingleton & operator = (const CSingleton &);
public:
	static CSingleton & GetInstance()
	{
		static CSingleton instance;   //局部静态变量
		return instance;
	}
};
```