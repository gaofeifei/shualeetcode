#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/26 7:47
# @Author  : feifeigao
# @File    : 26.py
"""
"""
26:
[题意]
删除有序数组中的重复项
[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]

"""

def a(nums):
    n=len(nums)
    j=0
    for i in range(n):
        if nums[i]!=nums[j]:
            j+=1
            nums[j] = nums[i]
    return  j+1






if __name__ == '__main__':
    nums= [1,2,3,3,3]
    r=a(nums)
    print(r)

