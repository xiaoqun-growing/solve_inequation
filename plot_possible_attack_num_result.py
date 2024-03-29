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
    x1 = np.linspace(1, 10, 5000)
    alpha2 = np.linspace(0, 10, 5000)
    alpha3 = np.linspace(0, 10, 5000)
    tmp = []
    beta = np.linspace(1, 20, 5000)
    for beta_i in beta:
        # for x in x1:
        #     for a2 in alpha2:
        #         for a3 in alpha3:
        target_2 = 10.0/(math.pow(20,math.ceil(beta_i-1)))
        if beta_i == 1 :
            print('target of beta is 1',target_2)
        if beta_i >= 1.95 and beta_i <= 2.05:
            print('target of beta is 2',target_2)
        tmp.append(target_2)
    target = np.array(tmp)
    plt.plot(beta, target, label=r'x1 /(alpha2+alpha3)^beta-1')
    plt.ylabel('W')
    plt.xlabel('beta')
    plt.ylim((0, 20))
    plt.xlim((0, 3))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    plt.fill_between(beta, target, where= (20>=target), color='grey', alpha=0.5)
    plt.legend(loc='upper left')
    plt.title('plot zone of acquiring result of different attack numbers')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./plot zone of acquiring result')


if __name__ == "__main__":
    # root_list,three_metrics_target = compxte_and_jxdge()
    plot_figure()
