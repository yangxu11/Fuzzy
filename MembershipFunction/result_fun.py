# -*-coding:utf-8-*-

#路径的效益  分为3个等级  L：小  M：中   H：大
import matplotlib.pyplot as plt
import numpy as np

def L(x):
    if x<=0.2:
        return 0
    elif 0.2 < x <= 0.4:
        return 5*x - 1
    elif 0.4 < x <= 0.6:
        return -5*x + 3
    else:
        return 0

def M(x):
    return L(x-0.2)

def H(x):
    return L(x-0.4)

def main():
    x = np.linspace(0.1, 1.1, 1000)

    yL = np.array([])
    yM = np.array([])
    yH = np.array([])



    for k in x:
        yL = np.append(yL, np.linspace(L(k), L(k), 1))

    for k in x:
        yM = np.append(yM, np.linspace(M(k), M(k), 1))

    for k in x:
        yH = np.append(yH, np.linspace(H(k), H(k), 1))



    plt.figure()

    plt.plot(x, yL, color='blue')
    plt.plot(x, yM, color='gray')
    plt.plot(x, yH, color='red')

    plt.show()


if __name__ == '__main__':
    main()