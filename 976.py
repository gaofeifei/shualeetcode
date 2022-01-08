#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 20:24
# @Author  : feifeigao
# @File    : 976.py
"""


def largestPerimeter(nums):
    # 排序
    temp = sorted(nums, reverse=True)
    # print(temp)
    # 连续的3个数组建不了，就跳过第一个大的，逐次判断两边之和大于第三边
    for i in range(len(nums)-2):
        if temp[i]<temp[i+1]+temp[i+2]:
            return temp[i]+temp[i+1]+temp[i+2]
    return 0




if __name__ == '__main__':
    nums=[3,6,2,3]
    c=largestPerimeter(nums)
    print(c)