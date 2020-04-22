# -*-coding:utf-8-*-
import math

import matplotlib.pyplot as plt
import numpy as np

'''
分为5个等级  L3:低  M3：中  H3：高
'''

def gauss_fun(u,sig,x):
    #u = 0  # 均值μ
    #sig = math.sqrt(0.2)  # 标准差δ

    return np.exp(-(x - u) ** 2 / (2 * sig ** 2))

def L3(x):
    return gauss_fun(1,0.3,x)

def M3(x):
    return gauss_fun(2,0.3,x)

def H3(x):
    return gauss_fun(3,0.3,x)

def get_sw_weight(x):
    sw_weight=[]
    sw_weight.append(L3(x))
    sw_weight.append(M3(x))
    sw_weight.append(H3(x))

    return sw_weight

def main():
    x = np.linspace(0, 4, 1000)

    yL3 = np.array([])
    yM3 = np.array([])
    yH3 = np.array([])


    for k in x:
        yL3 = np.append(yL3, np.linspace(L3(k), L3(k), 1))



    for k in x:
        yM3 = np.append(yM3, np.linspace(M3(k), M3(k), 1))

    for k in x:
        yH3 = np.append(yH3, np.linspace(H3(k), H3(k), 1))




    plt.figure()
    plt.plot(x, yL3, color='blue')
    plt.plot(x, yM3, color='gray')
    plt.plot(x, yH3, color='orange')


    plt.show()


if __name__ == '__main__':
    main()