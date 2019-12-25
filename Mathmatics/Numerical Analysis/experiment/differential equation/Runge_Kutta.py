import math
import numpy as np
import matplotlib.pyplot as plt

#===================================================================
# 数值积分的方法求解微分方程的初值解
# 比较方法：1. 龙格-库塔法 funtion runge_kutta；2. 欧拉法 function euler(); 3. 改进欧拉法（梯形法）：function enhanced_euler()
#===================================================================

def runge_kutta(y, x, dx, f):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """
    k1 = dx * f(y, x)
    k2 = dx * f(y + 0.5 * k1, x + 0.5 * dx)
    k3 = dx * f(y + 0.5 * k2, x + 0.5 * dx)
    k4 = dx * f(y + k3, x + dx)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.

def euler(y, x, dx, f):
    """
    欧拉法，
    :return:
    """
    return y + dx * f(y, x)


def enhanced_euler(y, x, dx, f):
    """
    改进欧拉法，一次迭代欧拉法
    :return:
    """
    y_plus_euler = y + dx * f(y, x)
    return y + dx / 2 * (f(y, x) + f(y_plus_euler, x + dx))

def func(y, x):
    """
    微分方程：dy/dx = func(y, x)
    :param y:
    :param t:
    :return:
    """
    return x * math.sqrt(y)

if __name__=='__main__':
    t = 0.0
    y_rk = 1.0
    y_euler = 1.0
    y_enhanced_euler = 1.0

    dt = 0.1
    ts = []
    y_rk_list, y_euler_list, y_enhanced_euler_list = [],[],[]
    while t <= 20:
        y_rk = runge_kutta(y_rk, t, dt, func)
        y_rk_list.append(y_rk)

        y_euler = euler(y_euler, t, dt, func)
        y_euler_list.append(y_euler)

        y_enhanced_euler = enhanced_euler(y_enhanced_euler, t, dt, func)
        y_enhanced_euler_list.append(y_enhanced_euler)

        t += dt
        ts.append(t)

    exact = [(t ** 2 + 4) ** 2 / 16. for t in ts]
    plt.plot(ts, y_rk_list, label='runge_kutta')
    plt.plot(ts, y_euler_list, label='naive euler')
    plt.plot(ts, y_enhanced_euler_list, label='enhanced euler')
    plt.plot(ts, exact, label='exact')
    plt.legend()
    plt.show()
    rk_error = np.array(exact) - np.array(y_rk)
    euler_error = np.array(exact) - np.array(y_euler)
    enhanced_error = np.array(exact) - np.array(y_enhanced_euler)
    print("runge kutta's max error {:.5f}".format(max(rk_error)))
    print("euler's max error {:.5f}".format(max(euler_error)))
    print("enhanced euler's max error {:.5f}".format(max(enhanced_error)))
