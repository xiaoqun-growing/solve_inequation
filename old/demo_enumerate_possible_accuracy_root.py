# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time

def compute_and_judge():
    x = 0.8
    y = 0
    z = 0.8
    n = 1
    root = []
    root_list = []
    three_metrics_target = []
    while n < 3000000:
        root = []
        if (1-x)*(1-y)*(1-z)<= 0.001:
            if 0 < x-z <1 and 0 < x-y <1 and z>= 0.8 and 0 < x < 1 :
                target_metrics = 1-(1-x)*(1-y)*(1-z)
                root.append(x)
                root.append(y)
                root.append(z)
                print('root',root)
                root_list.append(root)
                three_metrics_target.append(target_metrics)
        x = float(random.choice(np.arange(0.8,1,0.001)))
        y = float(random.choice(np.arange(0,1,0.0001)))
        z = float(random.choice(np.arange(0.8,1,0.001)))
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
    x_list = []
    y_list = []
    z_list = []
    for root in root_list:
        x_list.append(root[0])
        y_list.append(root[1])
        z_list.append(root[2])
    xd = np.array(x_list)
    yd = np.array(y_list)
    zd = np.array(z_list)
    ax1.scatter3D(xd,yd,zd, cmap='Blues')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    ax1.set_title('possible accuracy rate root')
    # ax1.plot_surface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./scatter3D_demo-{}.jpeg'.format(current_time))


if __name__ == "__main__":
    root_list,three_metrics_target = compute_and_judge()
    plot_figure(root_list,three_metrics_target)
