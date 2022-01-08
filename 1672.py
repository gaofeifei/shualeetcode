#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 20:12
# @Author  : feifeigao
# @File    : 1672.py
"""
"""
1672. 最富有客户的资产总量

"""

def a(nums):
    n=len(nums)
    l1=[]
    # print(n)
    for i in range(n):
        # print(nums[i])
        # sum(nums[i])
        # print(sum(nums[i]))
        l1.append(sum(nums[i]))
    print(l1)
    return max(l1)

if __name__ == '__main__':
    nums= [[1,2,3],[3,2,1]]
    nums= [[1,5],[7,3],[3,5]]
    nums= [[2,8,7],[7,1,3],[1,9,5]]
    r=a(nums)
    print(r)

