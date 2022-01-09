#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/9 20:04
# @Author  : feifeigao
# @File    : 1260.py
"""
"""
1260. 二维网格迁移

思路：先转成1维，挪动，再转回原来维度
"""


def a(nums,k):
    s=len(nums)
    #1转成一维
    total = nums[0]
    m,n=len(nums),len(nums[0])
    move = k % (m * n)
    for i in range(1, s):
        total += nums[i]
    print(total)
    #2挪动k位
    nuo=total[-move:]+total[:-move]
    print(nuo)

    #3再转成m*n的矩阵
    l2 = []
    for i in range(m):
        # print(i)
        l2.append(nuo[n * i:n * i + n])
    print(l2)
    return l2




if __name__ == '__main__':
    nums= [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    a(nums,k)

