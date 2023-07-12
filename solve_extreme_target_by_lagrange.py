# coding=utf-8
import random 
from scipy.optimize import derivative
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import time
import math
import json
import traceback


def factorial(start,end):   
    res = 1
    for i in np.arange(start, end+1):
    # for i in range(start, end+1):
        res *= i
    return res


def target(eta,mu1,mu2,mu3):
    numerator = 10*eta*math.factorial(mu1)*math.factorial(mu1+mu2*mu3-eta)
    denominator = math.factorial(mu1-eta)*math.factorial(mu1+mu2*mu3)
    result = numerator / denominator
    return result

def constraints(eta,mu1,mu2,mu3):
    con1 = mu1-eta
    con2 = 1-mu3
    con3 = mu3
    con4 = mu1+mu2-eta
    return con1,con1,con3,con4

# def solve():
#     eta= mu1,mu2,mu3
#     f = target(eta,mu1,mu2,mu3)
#     pass

