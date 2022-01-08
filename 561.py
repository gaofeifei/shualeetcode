#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 13:55
# @Author  : feifeigao
# @File    : 561.py
"""
def arrayPairSum(nums):

    n=len(nums)
    if n%2!=0 or n<2:return 0
    l1=sorted(nums)
    s=0
    #小的和小的凑一起，大的和大的凑一起
    for i in range(0,n,2):
        s+=l1[i]
    print(s)
    return s

if __name__ == '__main__':
    nums=[1,5,2,4,1,2]
    nums=[6,2,6,5,1,2]
    r=arrayPairSum(nums)
    print(r)