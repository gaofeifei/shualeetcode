#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 14:59
# @Author  : feifeigao
# @File    : 172.py
"""
"""
172. 阶乘后的零
[题意]
    给定一个整数 n ，返回 n! 统计结果中末尾零的数量。
[解题步骤]
    1递归终止条件必写防止死循环
    2递归参数传递，注意每次参数都不一样
    3递推式的推导
    4调用递归，传参，统计递归结果末尾0的个数
[思路题解]
    用递归解，之后的结果统计出0的个数

[tips]

[注意]

"""

def trailingZeroes(n):
    #终止条件
    if n<5:
        return 0
    # print(n/5+trailingZeroes(n/5))
    #找出所有5的倍数
    return n//5+trailingZeroes(n//5)



if __name__ == '__main__':
    n = 5
    r=trailingZeroes(n)
    print(r)

