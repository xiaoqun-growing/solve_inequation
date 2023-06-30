# coding=utf-8
import random 
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math
from sympy import symbols,diff,solve
import cvxpy 


def compxte_and_jxdge():
    # 物理域漏报率
    # x = 0.15
    # # 控制域漏报率
    # y = 0
    # 信息域漏报率
    # x1 = 10.0
    # alpha2 = 10.0
    # alpha3 = 10.0
    # beta = symbols('beta')
    # la = symbols('lambda')
    # target = x1/(math.pow(alpha2+alpha3,beta-1)) + la*(beta-alpha2+alpha3)
    # diff_3 = diff(target,beta)
    # diff_4 = diff(target,la)
    beta = cvxpy.Parameter(1,name='beta')
    p = beta - 1
    target = 10/cvxpy.power(20,p)
    obj = cvxpy.Maximize(target)
    constrain_1 = beta-20
    constraints = [constrain_1<=0.0,beta>=1]
    problem = cvxpy.Problem(obj,constraints)
    print("solve", problem.solve())  # Returns the optimal value.
    print("status:", problem.status)
    print("optimal value p* =", problem.value)
    print('optimal var: beta =',beta.value)

    return 

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
    # for beta_i in beta:
    #     for x in x1:
    #         for a2 in alpha2:
    #             for a3 in alpha3:
    #                 target_2 = x/(math.pow(a2+a3,beta_i-1))
    #                 if beta_i < 5.5 and beta_i > 4.75:
    #                     print('target of beta is 5',target_2)
    #                 tmp.append(target_2)
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
    compxte_and_jxdge()
