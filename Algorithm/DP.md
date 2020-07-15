---
title: DP 相关问题
date: 2020-06-18 20:39:00
categories:
- Algorithm
tags:
- Algorithm
---

# DP相关问题

## 题号

1. LC32 Longest Valid Parentheses
- 采用栈和DP，栈用来保存当前已经匹配的index
- 注意：input: `()(())` output: 6 

2. LC53 Maximum Subarray
- Transition function: `dp[i]=max{dp[i-1]+nums[i], nums[i]}`, `dp[i]` 代表 `nums[i]`参与的当前subarray的最大值

3. LC95 Unique Binary Search Trees II
- `DP` Transition function: `dp[i]=dp[0]*dp[i-1]+...+dp[i-1]*dp[0]`
- 主要思想是遍历0-n-1，取其中任意一个当做root的情况的总和
4. LC131 Palindrome Partitioning

5. LC132 Palindrome Partitioning II

6. LC1278 Palindrome Partitioning III

7. LC139 Word Break

8. LC140 Word Break II
9.  LC121
10. LC122
11.  LC123
12.  LC188
13.  LC643
14. LC644
15. LC1335
16. LC1326
17. LC42
18. LC1320 Minimum Distance to Type a Word Using Two Fingers
19. LC1310 XOR Queries of a Subarray
20. LC1312  Minimum Insertion Steps to Make a String Palindrome
- 普通DP？
21. LC5 Longest Palindromic Substring
- `Brute Force`带来较多的重复比较（判断 Palindromic 的时候）
- 采用 `(l,r)是Palindromic && s[l-1]==s[r+1]`遍历选取中心点 i，得到最大的 `len`
22. LC1143 Longest Common Subsequence
- 状态：`f[i][j]` 
```c++
if(text1[i-1] == text2[j-1])
    f[i][j] = max({f[i-1][j-1]+1, f[i-1][j], f[i][j-1]});
else
    f[i][j] = max(f[i-1][j], f[i][j-1]);
```

## 总结

### 动态规划

### 两个问题
- 状态
- 转移

### 记忆化递归与DP

记忆化递归与DP其实是一回事儿，主要是通过利用前面计算的结果加速当前计算。

- 递归
- 记忆化递归是 `Top-Down`
- DP是 `Bottom-Up`
单纯直接思考 `DP` 的做法有些弯路，可以按照 `递归->记忆化递归->Dynamic Programming` 的方式

## 参考

- [动态规划相关题目汇总](https://zhuanlan.zhihu.com/p/35707293)