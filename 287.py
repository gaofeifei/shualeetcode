#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 15:34
# @Author  : feifeigao
# @File    : 287.py
"""
"""
287:
[题意]
nums 只有 一个重复的整数 ，找出 这个重复的数
[思路题解]
排序之后，前一项=后一项，值就是重复的。因为排序后相同的值会挨着

[解题步骤]

[经典代码模板]

[tips]

[注意]

"""

def a(nums):
    n=len(nums)
    nums.sort()
    print(nums)
    for i in range(1,n):
        if nums[i-1]==nums[i]:
            return nums[i-1]

if __name__ == '__main__':
    nums= [1,3,4,2,2]
    r=a(nums)
    print(r)
