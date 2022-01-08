#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 15:16
# @Author  : feifeigao
# @File    : 455.py
"""


def findContentChildren(g, s):
    g.sort()
    s.sort()
    lg=len(g)
    ls = len(s)
    i=lg-1
    j=ls-1
    count=0
    while i>=0 and j>=0:
        if g[i]<=s[j]:
            count +=1
            i-=1
            j-=1
        else:
            i-=1
    return count

if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    g = [1, 2,8]
    s = [2, 7]
    r=findContentChildren(g, s)
    print(r)
