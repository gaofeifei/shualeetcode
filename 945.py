#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 14:18
# @Author  : feifeigao
# @File    : 945.py
"""

def minIncrementForUnique(nums):
    # 贪心算法
    nums.sort()
    count = 0
    print(nums)
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            count += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1
    print(nums)
    return count


if __name__ == '__main__':
    nums=[3,2,1,2,1,7,9]
    nums=[3,2,1,2,1,7]
    r=minIncrementForUnique(nums)
    print(r)