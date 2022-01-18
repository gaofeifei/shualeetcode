#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 23:54
# @Author  : feifeigao
# @File    : 剑指 Offer 03.py
"""
"""
剑指 Offer 03:数组中重复的数字
[题意]

[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]


"""
from collections import Counter
def a(nums):
    c=Counter(nums)
    l1=[]
    # print(c.most_common())
    for i,v in  c.most_common():
        # print(i,v)
        if v >=2:
            l1.append(i)
    # [int(x) for x in l1]
    return l1




if __name__ == '__main__':
    nums= [2, 3, 1, 0, 2, 5, 3]
    r=a(nums)
    print(r)

