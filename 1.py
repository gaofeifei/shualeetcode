#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 10:31
# @Author  : feifeigao
# @File    : 1.py
"""
"""
1. 两数之和

在该数组中找出 和为目标值 target  的那两个整数，并返回它们的数组下标。
nums[i]=target-nums[j]

"""
# 方法1
def a(nums,target):
    n=len(nums)
    l1=[]
    # print(nums)
    for i in range(n):
        cha=target-nums[i]
        if cha in nums:
            print(cha)
            #返回列表元素下标
            j=nums.index(cha)
            if j!=i:
                l1.append(j)
                l1.append(i)
    l1=list(set(l1))
    return l1

# 方法2
def b (nums,target):
    k={}#字典
    n=len(nums)
    for i in range(n):
        cha=target-nums[i]
        if cha in k:
            print(k[target - nums[i]])
            return [k[target - nums[i]], i]
        #不重复的逐个添加
        k[nums[i]]=i



if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 2, 4,3]
    target = 6
    # nums = [3, 3]
    # target = 6
    # r=b(nums,target)
    r = a(nums, target)
    print(r)

