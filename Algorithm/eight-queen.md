---
title: 八皇后问题
date: 2020-04-28 9:46:00
categories:
- Algorithm
tags:
- Algorithm
---

# 八皇后问题

## 回溯法

```python
class solution(object):

    def solveNQueens(self, n):
        # [-1, -1 ....]
        self.helper([-1] * n, 0, n)

    def helper(self, columnPosition, rowindex, n):  # ding
        # print(rowindex)
        if rowindex == n:
            self.printSolution(columnPosition, n)
            # print(columnPosition)
            return
        # for column in range(n-rowindex):
        for column in range(n):
            columnPosition[rowindex] = column
            # columnPosition[0] = 0
            if self.isValid(columnPosition, rowindex):
                self.helper(columnPosition, rowindex + 1, n)

    def isValid(self, columnPosition, rowindex):
        if len(set(columnPosition[:rowindex + 1])) != len(columnPosition[:rowindex + 1]):
            # print(columnPosition, rowindex)
            return False
        for i in range(rowindex):
            if abs(columnPosition[i] - columnPosition[rowindex]) == int(rowindex - i):
                # print(columnPosition, rowindex)
                return False
        return True

    def printSolution(self, columnPosition, n):
        # print(columnPosition)
        for row in range(n):
            line = ""
            for column in range(n):
                if columnPosition[row] == column:
                    line += "Q\t"
                else:
                    line += ".\t"
            print(line, "\n")
        print('\n')


solution().solveNQueens(8)
```