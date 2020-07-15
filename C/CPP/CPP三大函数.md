---
title: CPP 三大函数
date: 2020-05-27 23:52:00
categories:
- C
- CPP
tags:
- C
- CPP
---

# C++ 中的三大函数

当 Object with pointer member时，通常往往需要 override BigThree；当 Object without pointer member时，compiler 默认的 BigThree 已足够。注：除 BigThree 外，compiler 会为 Object 添加默认构造函数，且 compiler 添加的隐含函数往往执行效率较高。

```c++
class base {
public:
    base()=default;
    base(const string& a):name(a) {
        cout<<"const string& a"<<endl;
    }
    base(const base& b) {
        cout<<"const base& b"<<endl;
    }
    base& operator=(const base& b) {
        cout<<"operator =(const base& b)"<<endl;
        return *this;
    }
    ~base() {
        cout<<"~base"<<endl;
    }
private:
    string name;
};
```

## 默认构造

> 当类不包含任何构造函数时，编译器会自动生成无参数，函数体为空的默认构造函数；
> 
> 当类没有定义拷贝构造函数时，编译器会生成默认拷贝构造函数，此时属于浅拷贝

当程序员自定义了任意一种构造函数时，`默认构造` 则不被 compiler 自动生成，需要程序员显式写出；如代码中：

```c++
    base()=default;
    base(const string& a):name(a) {
        cout<<"const string& a"<<endl;
    }
```

但又出于性能方面及工作量方面的的考虑，`c++2.0` 引入 `Defaulted函数`即：`=default` 形仍旧使用 compiler 生成的默认构造函数。
注：
- `const string& a` 中的 `const` 要加上，否则 `base B = string("string");` 编译不通过；
- 尽量使用 `name(a)`

## 拷贝构造

拷贝构造函数，发生在拷贝构造期间，代码如下：

```c++
    base(const base& b) {
        cout<<"const base& b"<<endl;
    }
    // 或
    base(const base& b) = default;
```

常见的调用形式为：

```c++
    base A = B;         // 注意这种声明时初始化属于 拷贝构造，不属于拷贝复制
    base A(B);
```

## 拷贝复制

拷贝复制发生在两个已声明 Object 之间的复制，代码如下：

```c++
    base& operator=(const base& b) {
        cout<<"operator =(const base& b)"<<endl;
        return *this;
    }
    // 或
    base& operator=(const base& b) = default;
```

常见的调用形式为：

```c++
    base C;             //  显式的默认构造
    C = A;              //  拷贝复制
```

## `defaulted 函数`

`defaulted` 函数的几个限制：
- 仅适用于类的特殊成员函数，且该类成员函数没有默认参数；

```c++
    base(const string& a)=default;      // 错误
```
- `defaulted` 函数既可以 inline 定义，也可以 out-of-line 定义；

## 析构函数

```c++
    ~base() {
        cout<<"~base"<<endl;
    }
```

将虚构函数定义为非虚函数时，会存在内存泄漏的状况，代码如下：

```c++
class X {
private:
    int x;
};

class Y: public X {
private:
 int y;
};

int main(){
 X* x = new Y;
 delete x;          // 仅销毁了 x 指向的派生类对象中的基类子对象，存在内存泄漏
}
```

因此，常将基类的析构函数声明为虚函数，但由于存在程序员的工作量较大及函数执行效率较低的原因，使用 `=default`。

## `deleted` 函数

### 存在的意义

当我们在 `Singleton` 模式中想禁用掉：默认构造函数、拷贝构造函数、拷贝复制函数时，一个常用的方法是将这些函数声明在 `private` 关键字内；但这种方法存在：当友元类/成员函数还是可以访问这些函数

可以使用 `=delete` 将这些函数禁用，

### 用法

- 类的成员函数都可以通过 `=delete` 禁用掉，`=default` 仅限于类的特殊成员函数
- 必须在函数第一次声明时将声明为 `=delete` 函数，即：`=delete` 成员函数必须是 `inline`

## 参考

- [C++11 标准新特性：Defaulted 和 Deleted 函数](https://www.ibm.com/developerworks/cn/aix/library/1212_lufang_c11new/index.html)