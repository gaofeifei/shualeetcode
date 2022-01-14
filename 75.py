#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 14:44
# @Author  : feifeigao
# @File    : 75.py
"""
"""
75:
[题意]

[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]

"""

def sortColors(nums):
    n=len(nums)
    # return sorted(nums)
    # print(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    # print(nums)
    return nums


if __name__ == '__main__':
    # nums= [2,0,2,1,1,0]
    nums=[8,5,6,4,3,7,10,2]
    r=sortColors(nums)
    # print(r)

