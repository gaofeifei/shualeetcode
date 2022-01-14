#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 16:11
# @Author  : feifeigao
# @File    : 1608.py
"""
"""
1608:
[题意]
没太读懂
[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]

"""
#没过
def a(nums):
    n=len(nums)
    l1=set(nums)
    s=len(l1)
    # print(s)
    l2=list(l1)
    # l2.sort()
    # print(l2)
    for i in l2:
        if i<s:
            return -1
        else:return s


if __name__ == '__main__':
    nums= [0,4,3,0,4]
    # nums = [3, 6, 7, 7, 0]
    nums=[0,0]
    r=a(nums)
    print(r)
