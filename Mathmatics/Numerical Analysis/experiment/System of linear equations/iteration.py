# -*- coding: utf-8 -*-
"""
@title: 解线性方程组的迭代法
@link: https://blog.csdn.net/MachineRandy/article/details/82634730
@author: MachineRandy
@notation: 三种迭代方法：1. Jacobi 2. Gauss_Seidel 3. SOR
"""

import warnings
warnings.filterwarnings("ignore")

A1 = [
    [4,2,-4,0,2,4,0,0],
    [2,2,-1,-2,1,3,2,0],
    [-4,-1,14,1,-8,-3,5,6],
    [0,-2,1,6,-1,-4,-3,3],
    [2,1,-8,-1,22,4,-10,-3],
    [4,3,-3,-4,4,11,1,-4],
    [0,2,5,-3,-10,1,14,2],
    [0,0,6,3,-3,-4,2,19],
]

B1 = [0,-6,6,23,11,-22,-15,45]

A2 = [
      [10,3,1],
      [2,-10,3],
      [1,3,10],
]

B2 = [14,-5,14]

def jacobi(A,B,sigma,N):
    n = len(A)
    x0 = []
    x = []
    for i in range(0,n):
        x0.append(0)
        x.append(0)
    for k in range(1,N+1):
        R = 0
        for i in range(0,n):
            sum_ax = 0
            for j in range(0,n):
                sum_ax = sum_ax + A[i][j] * x0[j]
            x[i] = x0[i] + ((B[i] - sum_ax)/A[i][i])
            if abs(x[i] - x0[i]) > R:
                R = abs(x[i] - x0[i])
        if R <= sigma:
            print("精确度等于",sigma,"时，jacobi迭代法需要迭代",k,"次收敛")
            return (x,k)
        for i in range(0,n):
            x0[i] = x[i]
    return (x,k)

def gauss_seidel(A,B,sigma,N):
    n = len(A)
    x0 = []
    x = []
    for i in range(0,n):
        x0.append(0)
        x.append(0)
    for k in range(1,N+1):
        R = 0
        for i in range(0,n):
            sum_ax = 0
            for j in range(0,n):
                if j >= i:
                    sum_ax = sum_ax + A[i][j] * x0[j]
                else:
                    sum_ax = sum_ax + A[i][j] * x[j]
            x[i] = x0[i] + ((B[i] - sum_ax)/A[i][i])
            if abs(x[i] - x0[i]) > R:
                R = abs(x[i] - x0[i])
        if R <= sigma:
            print("精确度等于",sigma,"时，gauss_seidel迭代法需要迭代",k,"次收敛")
            return (x,k)
        for i in range(0,n):
            x0[i] = x[i]
    return (x,k)

def sor(A,B,sigma,N,omega):
    n = len(A)
    x0 = []
    x = []
    for i in range(0,n):
        x0.append(0)
        x.append(0)
    for k in range(1,N+1):
        R = 0
        for i in range(0,n):
            sum_ax = 0
            for j in range(0,n):
                if j >= i:
                    sum_ax = sum_ax + A[i][j] * x0[j]
                else:
                    sum_ax = sum_ax + A[i][j] * x[j]
            x[i] = x0[i] + omega * ((B[i] - sum_ax)/A[i][i])
            if abs(x[i] - x0[i]) > R:
                R = abs(x[i] - x0[i])
        if R <= sigma:
            print("精确度等于",sigma,"时，松弛因子为",omega,"时,sor迭代法需要迭代",k,"次收敛")
            print(x)
            return (x,k)
        for i in range(0,n):
            x0[i] = x[i]
    return (x,k)
jacobi(A2,B2,0.001,20)
jacobi(A2,B2,0.0001,20)
jacobi(A2,B2,0.00001,20)
gauss_seidel(A2,B2,0.001,20)
gauss_seidel(A2,B2,0.0001,20)
gauss_seidel(A2,B2,0.00001,20)
sor(A1,B1,0.001,2000,0.8)
sor(A1,B1,0.001,2000,0.9)
sor(A1,B1,0.001,2000,1)
sor(A1,B1,0.001,2000,1.1)
sor(A1,B1,0.001,2000,1.2)
"""   
(x,k) = jacobi(A2,B2,0.001,20)
(x1,k1) = gauss_seidel(A2,B2,0.001,20)
(x2,k2) = sor(A1,B1,0.001,40,1.5)
"""