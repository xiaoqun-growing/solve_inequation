import numpy as np
import matplotlib.pyplot as plt
import time

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
now = time.localtime(time.time())
current_time = time.asctime(now).replace(' ','_')
x = np.linspace(0, 1, 200)
plt.ylim((0, 1))
# 目标不等式函数 y=1-(80/(1-x)
plt.plot(x,1-(0.0125/(1-x)), label='y=1-(0.0125/(1-x))')
plt.plot(x, x, label='y=x')
plt.legend(loc='upper left')

plt.savefig('./Inverse proportional function_demo-{}.jpeg'.format(current_time))