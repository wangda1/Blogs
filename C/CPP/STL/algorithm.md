---
title: STL algorithm 总结
date: 2020-06-13 22:36:00
categories:
- C
- CPP
- STL
tags:
- C
- CPP
- STL
---

# Algorithm

## 常用函数

`find_if(words.begin(), words.end(), [sz](const string& a, const string& b) { return a.size() < b.size()});`
- 获取一个迭代器

`for_each(wc, words.end(), [](const string& s){cout<<s<<" ";});`

`stable_sort(words.begin(), words.end(), [](const string& a, const string& b) { return a.size() < b.size(); });`

`transform(vi.begin(), vi.end(), vi.begin(), [](int i) { return i < 0? -i : i;})`
- `transform接受三个迭代器和一个可调用对象。前两个迭代器表示输入序列，第三个迭代器表示目的位置。算法对输入序列中的每个元素调用可调用对象。`

`count_if(words.begin(), words.end(), [](int i) {return i%2==1;});`
- Returns the number of elements in the range [first,last) for which pred is true.
