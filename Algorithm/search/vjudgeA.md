---
title: 搜索与排序
date: 2020-06-16 20:16:00
categories:
- Algorithm
- search
tags:
- Algorithm
- search
---

# VjudgeA

- [vjudgeA](https://vjudge.net/contest/204422#problem/A)

这是一道比较常规的搜索题目，主要在于排序之后选取的搜索算法，这里采用二分查找，但由于要找到第一个值的index，所以进行了相应的改进。

```c++
//
// Created by wangc on 2020/6/16.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 二分查找
int binary_search(const vector<int>& searchv, const int& k) {
    int b = 0;
    int e = searchv.size() -1;
    int mid;
    while(b <= e) {
        mid = (b + e)/2;
        if (k <= searchv[mid])
            e = mid;
        else
            b = mid + 1;
        if (b == e) {
            if (searchv[b] == k)
                return b;
            else
                return -1;
        }
    }
    return -1;
}

int main() {
    int N, Q;
    cin>>N>>Q;
    int marbel_number, query_number;
    vector<int> marblev;
    for (int i = 0; i < N; ++i)
    {
        cin>>marbel_number;
        marblev.push_back(marbel_number);
    }
    sort(marblev.begin(), marblev.end());
    for (int i = 0; i < Q; ++i)
    {
        cin>>query_number;
        int index = binary_search(marblev, query_number);
        if (index == -1)
            cout<<query_number<<" not found"<<endl;
        else
            cout<<query_number<<" found at "<<index+1<<endl;

    }
    return 0;
}
```

但最终是 wrong answer 不知道为什么