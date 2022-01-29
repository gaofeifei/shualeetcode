#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/28 10:13
# @Author  : feifeigao
# @File    : 29.py
"""
"""
29:
[题意]

[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]

"""

def dividel(a,b):
    #取值范围
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
    if a == INT_MIN and b == -1:
        return INT_MAX
    if a == INT_MAX and b == 1:
        return INT_MAX
    if a == INT_MIN and b == 1:
        return INT_MIN
    if a == INT_MAX and b == -1:
        return INT_MIN
    # 判断符号赋值
    #同号异或为0假 异号异或为1真
    sign = -1 if (a > 0) ^ (b > 0) else 1
    print(sign)
    if a>=0:
        a=-a
    if b>=0:
        b=-b
    ans=0
    #除法就是做减法并将其所做减法次数累加
    while a<=b:
        a-=b
        ans+=1

    return ans if sign == 1 else -ans


if __name__ == '__main__':
    a, b=10,3
    a,b=-2147483648,-1
    a, b=2147483647,1
    a, b =-2147483648,1
    c=dividel(a, b)
    print(c)
    # d = 1^-3
    # print(type(d))
    # print(int("10000100", 2))

    # print(bin(1))
    # print(bin(2))
    # print(bin(3))
    # print(bin(4))
    # print(bin(5))
    # print(bin(6))
    # print("-----")
    # print(bin(-1))
    # print(bin(-2))
    # print(bin(-3))
    # print(bin(-4))
    # print(bin(-5))
    # print(bin(-6))



