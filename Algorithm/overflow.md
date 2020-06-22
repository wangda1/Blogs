---
title: c++ 数据溢出的问题
date: 2020-06-17 22:20:00
categories:
- Algorithm
tags:
- Algorithm
---

# 数据溢出

以前在做题的时候，没有考虑过数据溢出的问题，在做 [leetcode29](https://leetcode.com/problems/divide-two-integers/) 题目的时候，发现边缘情况是这道题的难点之一

```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (!divisor || (dividend == INT_MIN && divisor == -1)) return INT_MAX;
        long long res = 0;
        long long temp, td;
        bool neg = (dividend < 0) ^ (divisor <  0);
        unsigned int dividend_abs = dividend <  0 ?  -((unsigned int)(dividend)) : +((unsigned int)(dividend));
        divisor = abs(divisor);
        while(dividend_abs >=  divisor) {
            td = divisor;
            temp = 1;
            while(dividend_abs >= td) {
                td <<= 1;
                temp <<= 1;
            }
            res += temp>>1;
            dividend_abs -= td>>1;
        }
        return neg ? -res : res;
    }
};
```

主要几个测试用例：

- `INT_MIN` 为 -2147483648，使用 `abs()/labs()` 取绝对值的时候，得到的结果均为 `-2147483648`，因此取绝对值的代码为：

```c++
unsigned int dividend_abs = dividend <  0 ?  -((unsigned int)(dividend)) : +((unsigned int)(dividend));
```

```c++
-2147483648
1
// -2147483648

-2147483648
-1
// 2147483647
```

> 在C/C++语言中，不能够直接使用-2147483648来代替最小负数，因为这不是一个数字，而是一个表达式。表达式的意思是对整数21473648取负，但是2147483648已经溢出了int的上限，所以定义为（-INT_MAX -1）。