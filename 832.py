#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/9 11:11
# @Author  : feifeigao
# @File    : 832.py
"""
"""

832. 翻转图像
图片看成矩阵
水平翻转：将图片的每一行都进行reverse反转，
例如[1,1,0]变成[0,1,1]。
二进制元素反转图片即 0变成1,1变成0。[1,0,1]反转结果[0,1,0]

"""
def a(nums):
    # 先reverse再将0和1互换
    n=len(nums)
    col=len(nums[0])
    print(n,col)
    l1=[]
    # nums.reverse()
    # print(nums)
    for i in range(n):
        # print(nums[i])
        nums[i].reverse()
        # print(nums[i])
    # print(nums)#nums水平翻转成功
        #异或操作实现0和1互换,用1^ 数字实现
        for j in range(col):
            # print(nums[i][j])
            nums[i][j]=1^nums[i][j]
    print(nums)
    return nums



if __name__ == '__main__':
    nums= [[1,1,0],[1,0,1],[0,0,0]]
    nums = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    a(nums)
