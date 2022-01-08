#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 20:20
# @Author  : feifeigao
# @File    : 766.py
"""
"""
766 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。

"""

def a(nums):
    n=len(nums)
    col=len(nums[0])
    for i in range(1,n):
        for j in range(1,col):
            if nums[i-1][j-1] != nums[i][j]:
                return False
    return True



if __name__ == '__main__':
    nums=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    nums= [[1,2],[2,2]]
    r=a(nums)
    print(r)
