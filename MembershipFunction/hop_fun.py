# -*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

def hop_short(x):
    if x <= 5:
        return 1
    elif 5 < x < 7:
       return -0.5 * x + 3.5
    else:
        return 0


def hop_long(x):
    if x <= 5:
        return 0
    elif 5 < x < 7:
       return 0.5 * x - 2.5
    else:
        return 1

def get_hop_weight(hops):
    hop_weight = []
    hop_weight.append(hop_short(hops))
    hop_weight.append(hop_long(hops))
    return hop_weight

def main() :
    x = np.linspace(0, 9,100)

    y1 = np.array([])
    y2 = np.array([])

    for k in x:
        y1 = np.append(y1,np.linspace(hop_short(k),hop_short(k),1))

    for k in x:
        y2 = np.append(y2,np.linspace(hop_long(k),hop_long(k),1))
    plt.figure()
    plt.plot(x,y1,color='red',linewidth=2,linestyle='--')
    plt.plot(x,y2)
    plt.show()


if __name__ == '__main__':
	main()