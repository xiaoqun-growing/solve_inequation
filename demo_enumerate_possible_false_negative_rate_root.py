# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time

def compute_and_judge():
    # 物理域漏报率
    # x = 0.15
    # 控制域漏报率
    # y = 0
    # 信息域漏报率
    z = 0.2
    n = 1
    root = []
    root_list = []
    three_metrics_target = []
    x = np.linspace(0,0.2, 200)
    y = np.linspace(0,0.2,200)
    for x_i in x:
        for y_j in y: 
        # x = float(random.choice(np.arange(0,0.2,0.001)))
        # y = float(random.choice(np.arange(0,0.2,0.001)))
            root = []
            if x_i*y_j*0.2 <= 0.001:
                # if 1 > x_i > 0 and y_j > x_i > 0 and 0.2>x_i>0 :
                if 1 > x_i > 0 :
                    # target_metrics = (1-x_i)*(1-y_j)*()
                    root.append(x_i)
                    root.append(y_j)
                    # root.append(z)
                    if root[0] >= 0.1 and root[0] < 0.11:
                        print('root',root)
                    # print('root',root)
                    root_list.append(root)

    return root_list,three_metrics_target

def plot_figure(root_list,metrics_list):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    now = time.localtime(time.time())
    current_time = time.asctime(now).replace(' ','_')
    fig = plt.figure()
    # ax1 = plt.axes(projection='3d')
    x_list = []
    y_list = []
    # z_list = []
    for root in root_list:
        x_list.append(root[0])
        y_list.append(root[1])
        # z_list.append(root[2])
    xd = np.array(x_list)
    yd = np.array(y_list)
    # wd = np.array(z_list)
    plt.scatter(xd,yd, cmap='Blues')
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.ylim((0, 0.2))
    # plt.xlim((0, 0.2))
    # ax1.set_zlabel('z')
    plt.title('possible false negative rate root')
    # ax1.plot_surface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./feasible_fields_demo-{}.jpeg'.format(current_time))


if __name__ == "__main__":
    root_list,three_metrics_target = compute_and_judge()
    plot_figure(root_list,three_metrics_target)
