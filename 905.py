#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 16:54
# @Author  : feifeigao
# @File    : 905.py
"""

# for i,v in enumerate(nums):
    # print(i,v)
def sortArrayByParity(nums):
    if len(nums) < 2: return nums
    l1=[]
    l2=[]
    for i in range(len(nums)):
        if nums[i]%2==0:l1.append(nums[i])
        else:l2.append(nums[i])
    print(l1)
    print(l2)
    l1.extend(l2)
    print(l1)
    return l1





if __name__ == '__main__':
    nums=[3,1,2,4]
    sortArrayByParity(nums)
