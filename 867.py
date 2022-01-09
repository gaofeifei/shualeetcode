#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/9 13:54
# @Author  : feifeigao
# @File    : 867.py
"""
"""
867转置矩阵
矩阵的 转置 是指将矩阵的主对角线翻转
交换矩阵的行索引与列索引。


"""
def a(nums):
    n=len(nums)
    col=len(nums[0])
    print(n,col)
    # 注意n行,col列的位置,转置后col是行，n是列
    l1 = [[0 for _ in range(n)] for _ in range(col)]
    print(l1)
    for i in range(n):
        for j in range(col):
            l1[j][i]=nums[i][j]
    print(l1)
    return l1

if __name__ == '__main__':
    nums= [[1,2,3],[4,5,6],[7,8,9]]
    # nums= [[1,2,3],[4,5,6]]
    a(nums)

