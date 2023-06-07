# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math


def compute_and_judge():
    # 蜜罐数量
    x = 10
    # 真实设备数量
    y = 10
    # 攻击目标数量
    # z 
    root = []
    root_list = []
    # x = np.linspace(0,10, 11)
    # y = np.linspace(1,10, 10)
    
    z = np.linspace(1,20,30000)
    for z_i in z:
        root = []
        target_1 = math.pow((x+y),z_i) - 2
        target_2 = math.pow((x+y),z_i)
        target = float(target_1/target_2)
        if x+y >= z_i > 0 :
            root.append(z_i)
            root.append(target)
            root_list.append(root)

    return root_list

def plot_figure(root_list):
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
    plt.title('possible acquiring result of different attack numbers')
    # ax1.plot_surface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./possible acquiring result of different attack numbers.jpeg')


if __name__ == "__main__":
    root_list = compute_and_judge()
    plot_figure(root_list)
