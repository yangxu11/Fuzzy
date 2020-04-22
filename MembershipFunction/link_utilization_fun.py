# -*-coding:utf-8-*-
import math

import matplotlib.pyplot as plt
import numpy as np

'''
分为5个等级  LL:很低  L：低  M：中等  H：高   HH：很高
'''

def LL(x):
    if x <= 0.2:
        return 1
    elif 0.2 < x < 0.3:
        return -10*x + 3
    else:
        return 0

def L(x):
    '''''
    if x<=0.2:
        return 0
    elif 0.2 < x <= 0.35:
        return (1/0.15)*x - 0.2/0.15;
    elif 0.35 < x < 0.5:
        return -(1/0.15)*x + 0.5/0.15;
    else:
        return 0
    '''''
    return gauss_fun(0.35,0.1,x)

def M(x):
    #return L(x-0.2)
    return gauss_fun(0.55, 0.1, x)

def H(x):
    #return L(x-0.4)
    return gauss_fun(0.75, 0.1, x)

def HH(x):
    if x<=0.8:
        return 0
    elif 0.8 < x < 0.9:
        return 10*x -8
    else:
        return 1

def gauss_fun(u,sig,x):
    #u = 0  # 均值μ
    #u01 = -2
    #sig = math.sqrt(0.2)  # 标准差δ

    #x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
    return np.exp(-(x - u) ** 2 / (2 * sig ** 2))  #/ (math.sqrt(2 * math.pi) * sig)
    # print(x)
    # print("=" * 20)
    # print(y_sig)
    # plt.plot(x, y_sig, "r-", linewidth=2)
    # plt.grid(True)
    # plt.show()

def get_bw_weight(bw_used):
    bw_weight = []
    bw_weight.append(LL(bw_used))
    bw_weight.append(L(bw_used))
    bw_weight.append(M(bw_used))
    bw_weight.append(H(bw_used))
    bw_weight.append(HH(bw_used))
    return bw_weight

def main():
    x = np.linspace(0, 1, 1000)

    yLL = np.array([])
    yL = np.array([])
    yM = np.array([])
    yH = np.array([])
    yHH = np.array([])

    for k in x:
        yLL = np.append(yLL, np.linspace(LL(k), LL(k), 1))

    for k in x:
        yL = np.append(yL, np.linspace(L(k), L(k), 1))

    for k in x:
        yM = np.append(yM, np.linspace(M(k), M(k), 1))

    for k in x:
        yH = np.append(yH, np.linspace(H(k), H(k), 1))

    for k in x:
        yHH = np.append(yHH, np.linspace(HH(k), HH(k), 1))


    plt.figure()
    plt.plot(x, yLL, color='green')
    plt.plot(x, yL, color='blue')
    plt.plot(x, yM, color='gray')
    plt.plot(x, yH, color='orange')
    plt.plot(x, yHH, color='red')

    plt.show()


if __name__ == '__main__':
    main()
    #gauss_fun()