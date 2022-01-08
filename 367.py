#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/3 17:15
# @Author  : feifeigao
# @File    : 367.py
"""
import math
def isPerfectSquare(num):
    # print(pow(num, 0.5))
    # print(math.sqrt(num))
    # return float.is_integer(pow(num, 0.5))
    # return n > 0 and ((n & (-n)) == n)#是否2的幂
    i=1
    p=0
    while 1:
        p=i*i
        if p==num:return True
        if p>num:return False
        i+=1
    return False


if __name__ == '__main__':
    n=10
    r=isPerfectSquare(n)
    print(r)