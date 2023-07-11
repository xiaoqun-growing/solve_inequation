# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math
import matplotlib as mpl

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

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

def factorial(start,end):   
    res = 1
    for i in range(start, end+1):
        res *= i
    return res

def plot_figure1():
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure(figsize=(20, 10.5))
    # x1 = np.linspace(1, 10, 5000)
    # alpha2 = np.linspace(0, 10, 5000)
    # alpha3 = np.linspace(0, 10, 5000)
    target = []
    beta = np.linspace(1, 20, 5000)
    alpha = np.linspace(0.01, 0.99, 5)
    for alpha_i in alpha:
        tmp = []
        for beta_i in beta:
            flag1 = math.ceil(10-(1-alpha_i)*beta_i-1) 
            k2 = min(math.ceil(alpha_i*beta_i),math.ceil(10-(1-alpha_i)*beta_i))
            if flag1 > 0 and k2 > 0 :
                target_3 = 10.0/factorial(math.ceil(10-(1-alpha_i)*beta_i-1),10) + 10/factorial(1,k2)
                if beta_i == 1 :
                    print('target of beta is 1',target_3)
                if beta_i >= 1.95 and beta_i <= 2.05:
                    print('target of beta is 2',target_3)
                tmp.append(target_3)
        cur_target = np.array(tmp)
        target.append(cur_target)
    for i,cur_y in enumerate(target):
        cur_alpha = alpha[i]
        plt.plot(beta[:len(cur_y)], cur_y, label=f'x1 /alpha3(alph3-1)...(alpha3-((1-{cur_alpha})))beta-1) + x1/min({cur_alpha}beta,alpha3-(1-{cur_alpha})beta)...1')
    plt.ylabel('gain of attacker')
    plt.xlabel('numbers of attack targets')
    plt.ylim((0, 20))
    plt.xlim((0, 10))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    # plt.fill_between(beta, target, where= (20>=target), color='grey', alpha=0.5)
    plt.legend(loc='upper right')
    plt.title('plot zone of acquiring result of different attack numbers')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./plot zone of acquiring result-V6.jpg')


def plot_figure():
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure(figsize=(20, 10.5))
    beta = np.linspace(1, 20, 5000)
    alpha = np.linspace(0.01, 0.99, 100)
    target_beta = []
    real_alpha = []
    for alpha_i in alpha:
        for beta_i in beta:
            flag1 = math.ceil(10-(1-alpha_i)*beta_i-1) 
            k2 = min(math.ceil(alpha_i*beta_i),math.ceil(10-(1-alpha_i)*beta_i))
            if flag1 > 0 and k2 > 0 :
                target_3 = 10.0/factorial(math.ceil(10-(1-alpha_i)*beta_i-1),10) + 10/factorial(1,k2)
                if target_3 < 10:
                    target_beta.append(math.ceil(beta_i))
                    real_alpha.append(alpha_i)
                    break            
    plt.plot(real_alpha, target_beta, label=f'max gain with different trueness of honeypot')
    plt.ylabel('the number of attack targets')
    plt.xlabel('simulating metrics of honeypot')
    plt.ylim((0, 10))
    plt.xlim((0, 1))
    plt.legend(loc='upper right')
    plt.title('the number of attack targets at max gain starting decrease with different simulating metrics of honeypot')
    plt.savefig('./plot zone of acquiring result-V5.jpg')


def plot_figure2():
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    config = {
            'text.usetex': True,
            # 'text.latex.preamble': r'\usepackage{CJK}',  # 预先导入CJK宏包处理中文
    }
    plt.rcParams.update(config)
    plt.rcParams.update({'font.size': 22}) 
    noz = time.localtime(time.time())
    current_time = time.asctime(noz).replace(' ','_')
    fig = plt.figure(figsize=(15, 8.5))
    # x1 = np.linspace(1, 10, 5000)
    # alpha2 = np.linspace(0, 10, 5000)
    # alpha3 = np.linspace(0, 10, 5000)
    target = []
    beta = np.linspace(1, 20, 5000)
    tmp = []
    for beta_i in beta:
        flag1 = math.ceil(10-(1-0.95)*beta_i-1) 
        k2 = min(math.ceil(0.95*beta_i),math.ceil(10-(1-0.95)*beta_i))
        if flag1 > 0 and k2 > 0 :
            target_3 = 10.0/factorial(math.ceil(10-(1-0.95)*beta_i-1),10) + 10/factorial(1,k2)
            if beta_i == 1 :
                print('target of beta is 1',target_3)
            if beta_i >= 1.95 and beta_i <= 2.05:
                print('target of beta is 2',target_3)
            tmp.append(target_3)
    cur_target = np.array(tmp)
    target.append(cur_target)
    plt.plot(beta, cur_target, label=r'$\displaystyle\frac{x_1}{alpha_3!}'
                                        r'+ \frac{x_1}{min\{0.95*beta,alpha_3-0.05*beta\}!}$')
    plt.ylabel(r'攻击者收益')
    plt.xlabel('number of attack targets',fontsize=20,color="b")
    plt.ylim((0, 20))
    plt.xlim((0, 5))
    # plt.fill_between(y, x1, x2, where= (x2>=0) & (x1<y), color='grey', alpha=0.5)
    # plt.fill_between(beta, cur_target, where= (20>=cur_target), color='grey', alpha=0.5)
    plt.legend(loc='upper right')
    plt.title('the gain of attacker with different number of attack targets')
    # ax1.plot_sxrface(xd,yd,zd,rstride=0.005,cstride=0.005,cmap=plt.cm.cool)
    plt.savefig('./plot zone of acquiring result-V8.svg')
    #plt.show()

if __name__ == "__main__":
    # root_list,three_metrics_target = compxte_and_jxdge()
    # plot_figure()
    plot_figure2()
