# -*-coding:utf-8-*-
import time
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from scipy import integrate

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

from MembershipFunction import hop_fun
from MembershipFunction import link_utilization_fun as bw_fun
from MembershipFunction import result_fun as res_fun
# import MembershipFunction.hop_fun as hop_fun
# import MembershipFunction.link_utilization_fun as bw_fun
# import MembershipFunction.result_fun as res_fun




class FuzzyEvaluate():

    def __init__(self):
        self.rule = self.get_rule()
        self.hop_map = ['short', 'long']
        self.bw_map = ['LL', 'L', 'M', 'H', 'HH']
        self.res_map = {'L': 0, 'M': 1, 'H': 2}
        self.res = []

    # 专家规则制定
    def get_rule(self):
        rule = {}
        rule[('short', 'LL')] = 'L'
        rule[('short', 'L')] = 'L'
        rule[('short', 'M')] = 'M'
        rule[('short', 'H')] = 'H'
        rule[('short', 'HH')] = 'H'
        rule[('long', 'LL')] = 'L'
        rule[('long', 'L')] = 'M'
        rule[('long', 'M')] = 'M'
        rule[('long', 'H')] = 'H'
        rule[('long', 'HH')] = 'H'

        return rule

    def fuzzy_evaluate(self, bw_used, hops):
        hop_weight = []
        bw_weight = []

        hop_weight = hop_fun.get_hop_weight(hops)
        bw_weight = bw_fun.get_bw_weight(bw_used)

        res = [0, 0, 0]

        for i in range(0, len(hop_weight)):
            for j in range(0, len(bw_weight)):
                min_tmp = min(hop_weight[i], bw_weight[j])
                if (min_tmp == 0):
                    continue
                res_level = self.rule[(self.hop_map[i], self.bw_map[j])]
                if res[self.res_map[res_level]] == 0:
                    res[self.res_map[res_level]] = min_tmp
                else:
                    res[self.res_map[res_level]] = max(min_tmp, res[self.res_map[res_level]])
        self.res = res
        score = self.evaluate(res)
        return score
        #print score
        #self.plot_res(res)

    # 根据模糊指标更新结果的隶属函数
    def update_fun(self, x,res):
        #res = self.res
        return max(min(res_fun.L(x), res[0]), min(res_fun.M(x), res[1]), min(res_fun.H(x), res[2]))

    # 积分求解面积中值对应的评分
    def evaluate(self, res):
        x = np.linspace(0.1, 1.1, 100)
        area = 0
        # area = integrate.quad(self.update_fun,0.2,1)
        # return area
        for i in x:
            area = area + i * self.update_fun(i,res)
        half = area / 2
        for i in x:
            area = area - i * self.update_fun(i,res)
            if area <= half:
                return i
        return -1

    # 画出隶属函数图
    def plot_res(self, res):
        x = np.linspace(0.1, 1.1, 1000)
        y = np.array([])
        for k in x:
            y = np.append(y, np.linspace(self.update_fun(k, res), self.update_fun(k, res), 1))

        plt.figure()
        plt.plot(x, y, color='blue')
        plt.show()


if __name__ == '__main__':
    f = FuzzyEvaluate()
    time1 = time.time()
    for i in range(100):
        f.fuzzy_evaluate(0.7, 5)
    t = time.time()-time1
    print t
