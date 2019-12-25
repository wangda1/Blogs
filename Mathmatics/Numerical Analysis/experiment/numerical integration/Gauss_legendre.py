# 任意区间上对函数的积分
"""
Gauss-Legendre 型积分在任意区间中的积分。
"""
import math

def fun(x):
    return x * x

def main():
    GauThree = {0.7745966692: 0.555555556, 0: 0.8888888889}
    GauFive = {0.9061798459: 0.2369268851, 0.5384693101: 0.4786286705, 0: 0.5688888889}
    GauSum = 0.0
    print("Input a and b as two numbers(must promise a<b):")
    a = int(input("input a please:"))
    b = int(input("input b please:"))
    for key, value in GauThree.items():
        GauSum += fun(((b - a) * key + a + b) / 2) * value
        if (key > 0):
            GauSum += fun(((a - b) * key + a + b) / 2) * value
    GauSum = GauSum * (b - a) / 2
    print("GauThree Method:", GauSum)
    GauSum = 0.0
    for key, value in GauFive.items():
        GauSum += fun(((b - a) * key + a + b) / 2) * value
        if (key > 0):
            GauSum += fun(((a - b) * key + a + b) / 2) * value
    GauSum = GauSum * (b - a) / 2
    print("GauFive  Method:", GauSum)

if __name__ == '__main__':
    main()
