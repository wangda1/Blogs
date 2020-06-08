---
title: C++ 面向对象高级编程
date: 2020-02-11 22:50:00
categories:
- C
- CPP
tags:
- C
- CPP
---

# C++ 面向对象高级编程

## 几个比较成熟的设计准则

- 多使用 `initialization list`

```c++
complex (double r = 0, double i = 0)
    : re(r), im(i)
    {}
```

- 注意成员函数能否加上 `const`

```c++
double real () const { return re; }
```

- `inline` 多写无害，编译器会根据函数的复杂程度自动决定是否应该 `inline`；函数若在 class body 内定义完成，便自动成为 inline 候选人

- 尽量使用 `pass by reference`，少使用 `pass by value`，同时还要注意 `const` 是否加入
- 同理，尽量使用 `return by reference`, 少使用 `return by value`
- function 尽量 public, data 尽量 private
- 当 `static` 用在成员函数中时，没有 `this` 指针，因此只能修改 `static variable`，不能修改 `object variable`

- 兄弟之间互为友元，可以互相访问对方的 private data.

```c++

```

- 类模板（class template）与函数模板（function template）

```c++
// 类模板
template<typename T>
class complex
{
    public:
        complex (T r= 0, T i = 0)
            : re (r), im (i)
            {}
        ...
}

// 函数模板
template<class T> // or template<typename T>
// template<typename T>
inline
const T& min(const T& a, const T& b)
{
    return b < a ? b : a;
}

// 使用
// 类模板需要声明变量的类型：double
complex<double> c1(2.5, 1.5);
// 函数模板不需要声明变量类型：编译器自动推导
stone r1(2,3), r2(3,3), r3;
r3 = min(r1, r2);
```

- 相同 class 的各个 objects 互为 friends（友元）

```c++
inline
String::String(const String& str)
{
    m_data = new char[ strlen(str.m_data) + 1 ];
    strcpy(m_data, str.m_data);
}
```

- `new` 与 `delete`：`array new` -- `array delete`

```c++
inline
String::~String()
{
    delete[] m_data;
}
```

- 临时对象（temporary object）的声明与定义

```c++
complex();
complex(4, 5);
// 当程序执行到这一行的时候前面两个对象的生命周期结束
```

Class 的两种经典分类：
- Class without pointer member(s)
- Class with pointer member(s)

对于 `Class with pointer members`，要显式定义三大函数`Big Three`：拷贝构造函数、拷贝赋值函数、析构函数

```c++
// 拷贝构造函数
String(const String& str);

// 拷贝赋值函数
String& operator=(const String& str);

// 析构函数
~String();
```

显式地定义三大函数的原因是，编译器会自动为 class 添加默认的拷贝构造与拷贝赋值函数，两个函数的行为均为对 object 的逐个字节复制，这样会使 指针 指向同一个地址。析构函数是为了释放指针指向的地址空间，防止内存泄漏。（memory leak）

## `Static`内存布局

见 [CPP_advanced_programming_oop](./CPP_advanced_programming_oop.md)

### namespace

- using directive

`using namespace std;`

- using declaration

`using std::cout;`

### 未完待续

![C++ToBeContinued](./CPP_advanced_programming_oop/cpp_to_be_continued.png)

## OOP

### Reference

reference 的背后是编译器通过 pointer 实现的，但为了语法规定，制造出了*object和其reference的大小相同，地址也相同* 的假象。

```c
int x=0;
int& r = x;
sizeof(r) == sizeof(x)
&x == &r
```

![reference](./CPP_advanced_programming_oop/reference_0.png)

![reference](./CPP_advanced_programming_oop/reference_1.png)

### 类和类之间的关系

- Inheritance（继承）
- Composition（复合）
- Delegation（委托）

### Composition（复合）`has-a`

反映的是一种 `has-a` 的关系 <--> `Adapter` 模式

![adapter](./CPP_advanced_programming_oop/cpp_composition_adapter.png)

- composition下的构造与析构函数
- 由内而外的构造：先调用 `component` 的构造函数，再调用 `container` 的构造函数
- 由外而内的析构： 与构造顺序正好倒置

### Delegation（委托）. Composition By Reference

![c++_delegation](./CPP_advanced_programming_oop/cpp_delegation.png)

### Inheritance（继承）`is-a`

- `non-virtual`：不可以被重写（覆写）
- `virtual`：可以被重写（`override`）注意：`override`仅发生在虚函数的过程中；
- `pure-virtual`：一定需要被覆写

![inheritance](./CPP_advanced_programming_oop/inheritance_template_method.png)

## C++ OOP Advanced Programming（Part II）

### `explicit` keyword

![explicit](./CPP_advanced_programming_oop/explicit.png)

### Conversion Function（转换函数）

实话说，这部分我没看明白

![conversion_function](./CPP_advanced_programming_oop/conversion-function.png)

### pointer-like classes

`pointer-like` class 的主要特点是实现了对 `operator */->` 的重载

- 智能指针

    ![shared_ptr](./CPP_advanced_programming_oop/pointer_like_shared_ptr.png)

- 迭代器

    ![iterator](./CPP_advanced_programming_oop/pointer_like_iterator.png)

    ![iterator_imple](./CPP_advanced_programming_oop/pointer_like_iterator_detail_imple.png)

### function-like classess

`function-like class`即实现了对 `operator ()` 的重载  

![functor](./CPP_advanced_programming_oop/functor.png)

## template

### class template

![class_template](./CPP_advanced_programming_oop/class_template.png)

### function template

![function_template](./CPP_advanced_programming_oop/function_template.png)

### member template

`member template` 是一种对 `class` 的成员函数声明成 `template` 的方式，其实并不明白这种做法有什么用？？？

![member_template](./CPP_advanced_programming_oop/member_template.png)

![member_template](./CPP_advanced_programming_oop/member_template2.png)

## specialization

`template` 是一种对 `class` or `function` 泛化的过程，但这种泛化有时可能不是通用的，需要在针对某些特定的类型做特殊处理，这时就需要 `specialization`（特化）。 

### specialization

![specialization](./CPP_advanced_programming_oop/specialization.png)

### partial specialization（偏特化）

分为两种：

- 参数个数的偏：泛化参数的减少

![partial_specialization](./CPP_advanced_programming_oop/partial_specialization.png)

- 参数范围的偏：泛化参数的变化

![partial_specialization](./CPP_advanced_programming_oop/range_type_partial_specialization.png)

### 模板模板参数

![template_template_parameter](./CPP_advanced_programming_oop/template_template_parameter.png)

## Object Model

### 多态与虚函数的底层实现之 `vptr, vtbl`

![cpp_vptr_vbtl](./CPP_advanced_programming_oop/cpp_vptr_vtbl.png)

- 每个 Object 都会包含一个 `virtual pointer` -> `virtual table`，里面包含 `virtual function` 的地址

```c++
// 函数的调用过程 `C` 风格：
(*(p->vptr)[n])(p);
(*p->vptr[n])(p);
// -> [] 的优先级高于 * 哦
```

### 关于 `Dynamic Binding`

Dynamic Binding的三个条件:

1. 通过pointer/reference调用；
2. 函数为 virtual function；
3. 可以向上转型 upcast;

#### 一个关于静态绑定的例子

![static binding](./CPP_advanced_programming_oop/CPP_Static_Binding.png)

#### 动态绑定

![Dynamic_binding](./CPP_advanced_programming_oop/CPP_Dynamic_Binding.png)

### 关于 `const`

详见 [const keyword](./static_extern_const.md)

### `new` 与  `delete`

编译器如何编译 Object 的  `new` 与 `delete` 语句

```c++
// ctor  的执行过程
String*ps = new String("Hello");

void * mem  =  operator new(sizeof(String));       // 内部调用 malloc
ps  = static_cast<String*>(mem);
ps->String::String("Hello");

// dtor  的执行过程
delete ps;

String::~String(ps);
operator delete(ps);
```

#### 对 `operator  new`、`operator  delete`  的重载

**对全局 `operator new` 与  `operator delete` 的重载**

![operator new and delete](./CPP_advanced_programming_oop/operator_new_delete.png)

**对 `member operator new/delete` 的重载**

![operator_new_delete_overload](./CPP_advanced_programming_oop/operator_new_delete_overload.png)

![operator_new_delete_array_overload](./CPP_advanced_programming_oop/operator_new_delete_array_overload.png)