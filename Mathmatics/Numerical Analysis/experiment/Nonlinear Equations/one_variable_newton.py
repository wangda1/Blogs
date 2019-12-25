from sympy import *
# step为迭代步数，x0为初始位置，obj为要求极值的函数
def newtons(step, x0, obj):
    i = 1 # 记录迭代次数的变量
    x0 = float(x0) # 浮点数计算更快
    obj_deri = diff(obj, x) # 定义一阶导数，对应上述公式
    obj_sec_deri = diff(obj, x, 2) # 定义二阶导数，对应上述公式
    while i <= step:
        if i == 1:
            # 第一次迭代的更新公式
            xnew = x0 - (obj_deri.subs(x, x0)/obj_sec_deri.subs(x, x0))
            print('迭代第%d次：%.5f' %(i, xnew))
            i = i + 1
        else:
            #后续迭代的更新公式
            xnew = xnew - (obj_deri.subs(x, xnew)/obj_sec_deri.subs(x, xnew))
            print('迭代第%d次：%.5f' % (i, xnew))
            i = i + 1
    return xnew
x = symbols("x") # x为字符变量
result = newtons(50, 10, x**6+x)
print('最佳迭代的位置：%.5f' %result)