#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 15:10
# @Author  : feifeigao
# @File    : 1342.py
"""
"""
1342:将数字变成 0 的操作次数
[题意]
非负整数 num ，返回将它变成 0 共需要几步。 如果当前num是偶数先除以 2 ；奇数减去 1再除以2
[解题步骤]

[思路题解]
判断num奇偶性


[经典代码模板]

[tips]

[注意]
"""
def numberOfSteps(nums):
    if nums==1:return 1
    if nums==0:return 0
    if nums%2==0:#偶数
        return numberOfSteps(nums//2)+1
    else:#奇数
        return numberOfSteps(nums-1)+1


if __name__ == '__main__':
    nums= 123
    r=numberOfSteps(nums)
    print(r)

