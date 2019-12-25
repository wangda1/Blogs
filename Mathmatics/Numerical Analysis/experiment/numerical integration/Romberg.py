import numpy as np

'''
给定一个函数，如：f(x)= x^(3/2），和积分上下限a,b，用机械求积Romberg公式求积分。
参考：https://blog.csdn.net/weixin_42920648/article/details/83346289
'''
def func(x):
    return x**(3/2)

class Romberg:
    def __init__(self, integ_dowlimit, integ_uplimit):
        '''
        初始化积分上限integ_uplimit和积分下限integ_dowlimit
        输入一个函数，输出函数在积分上下限的积分

        '''
        self.integ_uplimit = integ_uplimit
        self.integ_dowlimit = integ_dowlimit



    def calc(self):
        '''
        计算Richardson外推算法的四个序列

        '''
        t_seq1 = np.zeros(5, 'f')
        s_seq2 = np.zeros(4, 'f')
        c_seq3 = np.zeros(3, 'f')
        r_seq4 = np.zeros(2, 'f')
        # 循环生成hm间距序列
        hm = [(self.integ_uplimit - self.integ_dowlimit) / (2 ** i) for i in range(0,5)]
        print(hm)
        # 循环生成t_seq1
        fa = func(self.integ_dowlimit)
        fb = func(self.integ_uplimit)
        # 梯形积分法得到的两点公式
        t0 = (1 / 2) * (self.integ_uplimit - self.integ_dowlimit) * (fa+fb)
        t_seq1[0] = t0

        for i in range(1, 5):
            sum = 0
            # 多出来的点的累加和
            for each in range(1, 2**i, 2):
                sum =sum + hm[i]*func( self.integ_dowlimit+each * hm[i])#计算两项值
            temp1 = 1 / 2 * t_seq1[i - 1]
            temp2 =sum
            temp =  temp1 + temp2
            # 求t_seql的1-4位
            t_seq1[i] = temp
        print('T序列：'+ str(list(t_seq1)))
        # 循环生成s_seq2
        s_seq2 = [round((4 * t_seq1[i + 1] - t_seq1[i]) / 3,6) for i in range(0, 4)]
        print('S序列：' + str(list(s_seq2)))
        # 循环生成c_seq3
        c_seq3 = [round((4 ** 2 * s_seq2[i + 1] - s_seq2[i]) / (4 ** 2 - 1),6) for i in range(0, 3)]
        print('C序列：' + str(list(c_seq3)))
        # 循环生成r_seq4
        r_seq4 = [round((4 ** 3 * c_seq3[i + 1] - c_seq3[i]) / (4 ** 3 - 1),6) for i in range(0, 2)]
        print('R序列：' + str(list(r_seq4)))
        return 'end'


rom = Romberg(0, 1)
print(rom.calc())