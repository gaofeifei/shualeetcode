#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/3 15:55
# @Author  : feifeigao
# @File    : 231.py
"""
def mi2(n):
    k = 1
    i=1
    if n <= 0: return False
    if n == 1: return True
    while i < 32:
        k *= 2
        if k == n:
            return True
        i+=1
        print(i)
    return False

def mi3(n):
    k = 1
    i=1
    if n <= 0: return False
    if n == 1: return True
    while i < 21:
        k *= 3
        if k == n:
            return True
        i+=1
        print(i)
    return False

if __name__ == '__main__':
    print(mi3(288))