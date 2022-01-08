#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 11:51
# @Author  : feifeigao
# @File    : 1827.py
"""
def minOperations(nums):
    #[1,5,2,4,1] 变成 [1,5,6,7,8] 每次对应元素加1，总共需要多少次
    #首先找到从哪开始增，第一次遇到的后面元素比前一个元素小或相等
    #因为每次加1所以 原sum(nums)-新sum(nums)=总累加操作次数
    n=len(nums)
    if n < 2: return 0
    print(nums)
    l=sum(nums)
    for i in range(n-1):
        if nums[i+1]<nums[i]:
            nums[i + 1]=nums[i]+1
    print(nums)
    r=sum(nums)
    return r-l



if __name__ == '__main__':
    nums=[1,5,2,4,1]
    r=minOperations(nums)
    print(r)
