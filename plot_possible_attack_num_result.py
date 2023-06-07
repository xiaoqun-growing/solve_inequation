# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math


def compxte_and_jxdge():
    # 物理域漏报率
    # x = 0.15
    # # 控制域漏报率
    # y = 0
    # 信息域漏报率
    z = 0.2
    n = 1
    root = []
    root_list = []
    three_metrics_target = []
    while n < 300:
        x = float(random.choice(np.arange(0,0.15,0.001)))
        y = float(random.choice(np.arange(0,1,0.001)))
        z = float(random.choice(np.arange(0,0.15,0.001)))
        root = []
        if (1-x)*(1-y)*(1-z) <= 0.01:
            if y > x > 0 and 0.2 > x > 0 and 0 < y < 1 :
                target_metrics = 1-(1-x)*(1-y)*(1-z)
                root.append(x)
                root.append(y)
                root.append(z)
                if root[2] > 0.1:
                    print('root',root)
                root_list.append(root)
                three_metrics_target.append(target_metrics)
        # y+=0.01
        # z+=0.01
        n+=1
    return root_list,three_metrics_target

def plot_figure():
    # y>x>0;0.2>x>0;
    # 0.8(1−x)(1−y)≤0.01
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure()
    y = np.linspace(0, 20, 5000)
    tmp = []
    z = np.linspace(0, 20, 5000)
    for z_i in z:
        target_1 = 1 - 2/(math.pow(2,z_i)*math.pow(10,z_i))
        target_2 = 1 - 2/(math.pow(2,z_i)*math.pow(10,z_i))
        if z_i < 5.5 and z_i > 4.75:
            print('target of beta is 5',target_1)
        tmp.append(target_1)
    x2 = np.array(tmp)

    plt.plot(y, x2, label=r'(x+y)^z-2 /(x+y)^z')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.ylim((0, 2))
    plt.xlim((0, 3))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    plt.fill_between(y, x2, where= (20>=y), color='grey', alpha=0.5)
    plt.legend(loc='upper left')
    plt.title('plot zone of acquiring result of different attack numbers')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./plot zone of acquiring result')


if __name__ == "__main__":
    # root_list,three_metrics_target = compxte_and_jxdge()
    plot_figure()
