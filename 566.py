#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/9 14:41
# @Author  : feifeigao
# @File    : 566.py
"""
"""
566. 重塑矩阵
行遍历顺序：正常的遍历顺序由左到右，逐行遍历
(1)首先判断原二维数组的行，列之积是否等于另一个新矩阵（r x c）的行列之积
(2)若他们积相等则整合成（r x c）行列矩阵并返回
(3)若不等则返回原矩阵
"""

def a(nums,r,c):
    n=len(nums)
    col=len(nums[0])
    # 是否能转
    if n*col!=r*c:
        return nums

    #二维降一维
    total = nums[0]
    for i in range(1, n):
        total+=nums[i]
    print(total)
    ans = []  # 然后分r次按照长度c把列表切片加入到ans中
    for i in range(r):
        ans.append(total[c * i:c * i + c])
        print(total[c * i:c * i + c])
    return ans




if __name__ == '__main__':
    nums= [[1,2],[3,4]]
    r = 1
    c = 4

    # nums=[[1, 2], [3, 4]]
    # r=4
    # c=1
    s=a(nums,r,c)
    print(s)

