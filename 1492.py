#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/3 16:40
# @Author  : feifeigao
# @File    : 1492.py
"""

def kthFactor(n,k):
    i=1
    count=0
    if n<=0:return -1
    if n==1 or k==1:return 1
    if k>n:return -1;
    while i<=n:
        if n%i==0:
            count+=1
            print("元素:"+str(i))
            if count==k:
                return i
        i+=1
    return -1


if __name__ == '__main__':
    n=4
    k=4
    r=kthFactor(n, k)
    print(r)