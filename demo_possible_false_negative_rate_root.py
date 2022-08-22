# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time

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
    y = np.linspace(0, 1, 500)
    x1 = y
    # x2 = 0.2
    x2 = 1-(0.0125/(1-y))

    plt.plot(y, x1, label=r'y > x > 0')
    plt.plot(y, x2, label=r'0.8(1-x)(1-y) <= 0.01')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.ylim((0, 1))
    plt.xlim((0, 1))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    plt.fill_between(y, x1, x2, where= (x2>=0), color='grey', alpha=0.5)
    plt.legend(loc='upper left')
    plt.title('possible false negatiye rate feasible fields')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./feasible fields_demo-{}.jpeg'.format(current_time))


if __name__ == "__main__":
    # root_list,three_metrics_target = compxte_and_jxdge()
    plot_figure()
