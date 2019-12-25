#coding=utf-8
"""
@title: 分段线性插值
@refer: https://cloud.tencent.com/developer/article/1423591
"""
from matplotlib import pyplot as plt
def DivideLine(data,testdata):
    #找到最邻近的
    data_x=[data[i][0] for i in range(len(data))]
    data_y=[data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        index=0
        for j in range(len(data_x)):
            if data_x[j]<testdata and  data_x[j+1]>testdata:
                index=j
                break
        predict=1.0*(testdata-data_x[j])*(data_y[j+1]-data_y[j])/(data_x[j+1]-data_x[j])+data_y[j]
        return predict

def plot(data,nums):
    data_x=[data[i][0] for i in range(len(data))]
    data_y=[data[i][1] for i in range(len(data))]
    Area=[min(data_x),max(data_x)]
    X=[Area[0]+1.0*i*(Area[1]-Area[0])/nums for i in range(nums)]
    X[len(X)-1]=Area[1]
    Y=[DivideLine(data,x) for x in X]
    plt.plot(X,Y,label='result')
    for i in range(len(data_x)):
        plt.plot(data_x[i],data_y[i],'ro',label="point")
    # plt.savefig('DivLine.jpg')
    plt.show()

data=[[0,0],[1,2],[2,3],[3,8],[4,2]]
print(DivideLine(data,1.5))
plot(data,100)