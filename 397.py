#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 19:52
# @Author  : feifeigao
# @File    : 397.py
"""
"""
397:整数替换
[题意]
给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？

[思路题解]
贪心 效率高些
递归
DFS深度优先搜索

[解题步骤]

[经典代码模板]

[tips]
偶数会比奇数少折腾(因为奇数还得+1或-1)
[注意]
1342相似

"""

def integerReplacement(nums):
    n=nums
    time=0
    while n!=1:#循环退出条件 是1就退出循环
        #n-1
        if n%2==1:#奇数
            temp=n-1
            #n+1
            if temp//2%2==1 and temp//2!=1:
                n+=1
            else:n=temp
        else:
            n=n//2#偶数
        time+=1
    return time

if __name__ == '__main__':
    nums = 8
    # nums = 7
    # nums = 4
    r=integerReplacement(nums)
    print(r)
