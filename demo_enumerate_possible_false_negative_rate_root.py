# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time

def compute_and_judge():
    # 物理域误报率
    u = 0.15
    # 控制域误报率
    v = 0
    # 信息域误报率
    w = 0.15
    n = 1
    root = []
    root_list = []
    three_metrics_target = []
    while n < 30000:
        root = []
        if (1-u)*(1-v)*(1-w) >= 0.85:
            if 0.15 >= w > u > 0 and v > u > 0 and 0 < v < 1 :
                target_metrics = 1-(1-u)*(1-v)*(1-w)
                root.append(u)
                root.append(v)
                root.append(w)
                if root[2] > 0.1:
                    print('root',root)
                root_list.append(root)
                three_metrics_target.append(target_metrics)
        u = float(random.choice(np.arange(0,0.15,0.001)))
        v = float(random.choice(np.arange(0,1,0.001)))
        w = float(random.choice(np.arange(0,0.15,0.001)))
        # y+=0.01
        # z+=0.01
        n+=1
    return root_list,three_metrics_target

def plot_figure(root_list,metrics_list):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    now = time.localtime(time.time())
    current_time = time.asctime(now).replace(' ','_')
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    u_list = []
    v_list = []
    w_list = []
    for root in root_list:
        u_list.append(root[0])
        v_list.append(root[1])
        w_list.append(root[2])
    ud = np.array(u_list)
    vd = np.array(v_list)
    wd = np.array(w_list)
    ax1.scatter3D(ud,vd,wd, cmap='Blues')
    ax1.set_xlabel('u')
    ax1.set_ylabel('v')
    ax1.set_zlabel('w')
    ax1.set_title('possible false negative rate root')
    # ax1.plot_surface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./scatter3D_demo-{}.jpeg'.format(current_time))


if __name__ == "__main__":
    root_list,three_metrics_target = compute_and_judge()
    plot_figure(root_list,three_metrics_target)
