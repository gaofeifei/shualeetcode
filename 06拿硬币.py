#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 20:43
# @Author  : feifeigao
# @File    : 06拿硬币.py
"""

def minCount(coins):
    n=len(coins)
    i=0
    count=0
    while i<n:
        if coins[i]%2==0:
            count+=coins[i]//2
        else:
            count += coins[i]//2 +1
        i+=1
    print(count)


if __name__ == '__main__':
    coins=[4,2,1]
    coins=[2,3,10]
    minCount(coins)









