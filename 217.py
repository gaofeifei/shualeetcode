#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 14:07
# @Author  : feifeigao
# @File    : 217.py
"""


def containsDuplicate(nums) -> bool:
    # 先排序，再比较，重复元素必相邻
    if len(nums) == 1 or len(nums) < 1: return False
    l1 = sorted(nums)
    print(l1)
    for i in range(1, len(nums)):
        # print(nums[i])
        if l1[i] == l1[i - 1]:
            print(str(l1[i]) + "\t" + str(l1[i - 1]))
            return True
    return False

if __name__ == '__main__':
    nums=[2,14,18,22,22]
    r=containsDuplicate(nums)
    print(r)