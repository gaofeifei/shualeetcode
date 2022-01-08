#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 11:30
# @Author  : feifeigao
# @File    : 1913.py
"""

def maxProductDifference(nums):
    # 2个最大的乘积减去2个最小的乘积
    i = len(nums)
    if i<4:return 0
    l1=sorted(nums)
    print(l1)
    r=l1[i-1]*l1[i-2]-l1[0]*l1[1]
    print(r)


if __name__ == '__main__':
    nums=[4,2,5,9,7,4,8]
    maxProductDifference(nums)
