#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 18:00
# @Author  : feifeigao
# @File    : 1351.py
"""
"""
1351. 统计有序矩阵中的负数
"""
def a(nums):
    #行
    n=len(nums)
    # print(n)
    #列
    col=len(nums[0])
    # print(len(nums[0]))
    count=0
    for i in nums:
        # print(i)
        for j in i:
            if j<0:
                count+=1
    # print(count)
    return count

if __name__ == '__main__':
    nums= [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    nums=[[3,2],[1,0]]
    nums=[[1,-1],[-1,-1]]
    nums=[[-1]]
    r=a(nums)
    print(r)

