#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 15:41
# @Author  : feifeigao
# @File    : 1941.py
"""
"""
1941:检查是否所有字符出现次数相同
[题意]

[思路题解]
模块导入from collections import Counter
Counter(nums)统计出每个元素的个数，返回 元素:个数 字典
遍历这个字典中元素对应的个数，将其放入列表中(也可直接放入set)
返回set的大小,为1全是相同的返回True 否则返回False
[解题步骤]

[经典代码模板]

[tips]

[注意]


"""
from collections import Counter
def a(nums):
    d1=Counter(nums)
    l1=[]
    for i,v in enumerate(d1):
        # print(d1[v])
        l1.append(d1[v])
    # print(l1)
    s=set(l1)
    n=len(s)
    if n==1:return True
    else:return False


if __name__ == '__main__':
    nums= "abacbc"
    nums= "aaabb"
    r=a(nums)
    print(r)

