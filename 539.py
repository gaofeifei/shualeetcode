#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 19:46
# @Author  : feifeigao
# @File    : 539.py
"""
def findMinDifference(timePoints):
    ms = []
    for t in timePoints:
        h, m = t.split(":")
        #转成分钟
        ms.append(int(h)*60+int(m))
    ms.sort()
    #print([i for i in zip(ms, ms[1:])])#23*60+59=1439
    # print([min(ms[-1] - ms[0], 24*60+ms[0]-ms[-1])])
    #zip打包为元组的列表
    return min([min(b - a, 24*60+a-b) for a, b in zip(ms, ms[1:])] + [min(ms[-1] - ms[0], 24*60+ms[0]-ms[-1])])

if __name__ == '__main__':
    timePoints=["23:59","00:00"]
    r=findMinDifference(timePoints)
    print(r)