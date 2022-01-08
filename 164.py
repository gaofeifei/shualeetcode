#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 15:43
# @Author  : feifeigao
# @File    : 164.py
"""


def maximumGap(nums) -> int:
    if len(nums) < 2: return 0
    l1 = sorted(nums)
    l2=[]
    print(l1)
    for i in range(1,len(nums)):
        # print(l1[i])
        cha=l1[i]-l1[i-1]
        # print(cha)
        if cha>=0:
            l2.append(cha)
    # print(l2)
    print(max(l2))
    return max(l2)

if __name__ == '__main__':
    nums=[3,6,9,1]
    nums=[4,7,21,3,2,36,58]
    nums=[4,7,21,36,58]
    nums=[1, 1, 1, 1]
    nums=[100,3,2,1]
    maximumGap(nums)