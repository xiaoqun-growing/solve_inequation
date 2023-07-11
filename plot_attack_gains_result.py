# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math

plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams.update({'font.size': 22}) 
plt.rcParams["figure.dpi"] = 120

def factorial(start,end):   
    res = 1
    for i in np.arange(start, end+1):
    # for i in range(start, end+1):
        res *= i
    return res

def factorial_new(num):   
    if (num == 1 or num == 0):
        return 1
    else: 
        return (num*factorial_new(num-1))


def plot_figure1():
    # 绘制三维散点图
    plt.rcParams.update({'font.size': 22}) 
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure(figsize=(25, 15))
    ax = fig.add_subplot(projection='3d')
    # beta = list(range(1,20,1))
    mu1 = list(range(1,10,1))
    mu2 = list(range(1,10,1))
    mu3 = np.linspace(0.10, 0.99, 9)
    for mu1_i in mu1:
        cur_beta = list(range(0,mu1_i,1))
        for mu2_i in mu2:
            for mu3_i in mu3:
                tmp = []
                for beta_i in cur_beta:
                    numerator = 10*beta_i*factorial(1, mu1_i)*factorial(1, mu1_i+mu2_i*mu3_i-beta_i)
                    denominator = factorial(1, mu1_i-beta_i)*factorial(1, mu1_i+mu2_i*mu3_i)
                    target_3 = numerator / denominator
                    if beta_i == 1 :
                        print('target of beta is 1',target_3)
                    if beta_i == 2:
                        print('target of beta is 2',target_3)
                    tmp.append(target_3)
                real_size = len(tmp)
                ax.scatter(cur_beta[:real_size], list(mu2*mu3)[:real_size], np.array(tmp), s=50, alpha=0.6)
    target = np.array(tmp)
    # plt.plot(beta, target, label=f'不同仿真度蜜罐的收益')
    ax.set_xlabel('攻击目标数量')
    ax.set_ylabel('蜜罐设备数量*蜜罐仿真度')
    ax.set_zlabel('攻击者收益')
    plt.legend(loc='best')
    # plt.title('the number of attack targets at max gain starting decrease with different simulating metrics of honeypot')
    plt.title('不同蜜罐仿真度下攻击收益随攻击数量的变化')
    plt.savefig('./不同蜜罐仿真度下攻击收益随攻击数量的变化.jpeg')


def plot_figure2():
    # 绘制多曲线分图
    # plt.rcParams.update({'font.size': 22}) 
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    # fig = plt.figure(figsize=(25, 15))
    mu1 = list(range(1,11,1))
    mu2 = list(range(1,11,1))
    mu3 = np.linspace(0.01, 0.99, 10)
    for mu1_i in mu1:
        cur_beta = list(range(0,mu1_i,1))
        for mu2_i in mu2:
            fig, axs = plt.subplots(4, 3)
            fig.tight_layout()
            for num,mu3_i in enumerate(mu3):
                tmp = []
                for beta_i in cur_beta:
                    numerator = 10*beta_i*factorial(1, mu1_i)*factorial(1, mu1_i+mu2_i*mu3_i-beta_i)
                    denominator = factorial(1, mu1_i-beta_i)*factorial(1, mu1_i+mu2_i*mu3_i)
                    target_3 = numerator / denominator
                    tmp.append(target_3)
                real_size = len(tmp)
                cur_target = np.array(tmp)
                row = int(num // 3)
                column = int(num % 3)
                axs[row,column].plot(cur_beta[:real_size], cur_target)
                axs[row,column].set_title(r'$\mu_1=%s,\mu_2=%s,\mu_3=%s$' % (mu1_i,mu2_i,round(mu3_i,2)),fontsize=8)
                # axs.title.set_size(8)
            for ax in axs.flat:
                ax.set(xlabel='攻击目标数量', ylabel='攻击者收益')
                ax.label_outer()
            plt.savefig(f'./different_factors_results/真实设备数量为{mu1_i}与蜜罐数量为{mu2_i}-不同蜜罐仿真度下攻击收益随攻击数量的变化.jpeg')
    # plt.ylim((0, 20))
    # plt.xlim((0, 5))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    # plt.fill_between(beta, cur_target, where= (20>=cur_target), color='grey', alpha=0.5)
    # plt.legend(loc='upper right')
    # plt.title('不同攻击目标数量的攻击者收益')
    # plt.savefig('./不同蜜罐仿真度下攻击收益随攻击数量的变化.jpeg')

def plot_figure3():
    plt.rcParams['font.sans-serif']=['SimHei']
    # plt.rcParams['axes.unicode_minus'] = False
    # config = {
    #         'text.usetex': True,
    #         # 'text.latex.preamble': r'\usepackage{CJK}',  # 预先导入CJK宏包处理中文
    # }
    # plt.rcParams.update(config)
    # plt.rcParams.update({'font.size': 22}) 
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure(figsize=(13, 7))
    target = []
    beta = list(range(1,20,1))
    tmp = []
    for beta_i in beta:
        numerator = 10*beta_i*factorial(1, 10)*factorial(1, 19.5-beta_i)
        denominator = factorial(1, 10-beta_i)*factorial(1, 19.5)
        target_3 = numerator / denominator
        if beta_i == 1 :
            print('target of beta is 1',target_3)
        if beta_i == 2:
            print('target of beta is 2',target_3)
        tmp.append(target_3)
    cur_target = np.array(tmp)
    plt.plot(beta, cur_target, label=r'$\frac{10 \eta 10! (19.5-\eta)!}{(10-\eta)! 19.5!}$')
    plt.ylabel('攻击者收益')
    plt.xlabel('攻击目标数量')
    plt.ylim((0, 20))
    plt.xlim((0, 5))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    # plt.fill_between(beta, cur_target, where= (20>=cur_target), color='grey', alpha=0.5)
    plt.legend(loc='upper right')
    plt.title('不同攻击目标数量的攻击者收益')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./不同攻击目标数量的攻击者收益-v2.jpeg')


def plot_figure4():
    # 绘制多曲线分图
    # plt.rcParams.update({'font.size': 22}) 
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    # fig = plt.figure(figsize=(25, 15))
    mu1 = list(range(1,11,1))
    mu2 = list(range(1,11,1))
    mu3 = np.linspace(0.01, 0.99, 10)
    for mu1_i in mu1:
        cur_beta = list(range(0,mu1_i+1,1))
        fig, axs = plt.subplots(5, 2, figsize=(15,12))
        fig.tight_layout()
        for num,mu2_i in enumerate(mu2):
            for mu3_i in mu3:
                tmp = []
                for beta_i in cur_beta:
                    numerator = 10*beta_i*factorial(1, mu1_i)*factorial(1, mu1_i+mu2_i*mu3_i-beta_i)
                    denominator = factorial(1, mu1_i-beta_i)*factorial(1, mu1_i+mu2_i*mu3_i)
                    target_3 = numerator / denominator
                    tmp.append(target_3)
                real_size = len(tmp)
                cur_target = np.array(tmp)
                row = int(num // 2)
                column = int(num % 2)
                axs[row,column].plot(cur_beta[:real_size], cur_target,label=f'{round(mu3_i,2)}')
                axs[row,column].legend(loc='upper right')
                axs[row,column].set_title(r'$\mu_1=%s,\mu_2=%s$' % (mu1_i,mu2_i),fontsize=8)
                print(f'({row},{column}):{mu3_i}')
            for ax in axs.flat:
                ax.set(xlabel='攻击目标数量', ylabel='攻击者收益')
                ax.label_outer()
        plt.savefig(f'./different_factors_results/second/真实设备数量为{mu1_i}-不同蜜罐数量及仿真度下攻击收益随攻击数量的变化.jpeg')


if __name__ == "__main__":
    # root_list,three_metrics_target = compxte_and_jxdge()
    # plot_figure()
    # plot_figure2()
    # plot_figure3()
    # plot_figure1()
    plot_figure4()
