#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/5 21:37
# @Author  : feifeigao
# @File    : 剑指58左旋转字符串.py
"""
def reverseLeftWords(s,k):
    print(s[:k])
    i=len(s)
    print(s[k:]+s[:k])




if __name__ == '__main__':
    # s="abcde"
    # k=2
    # s = "abcdefg"
    # k = 2
    s = "lrloseumgh"
    k = 6
    reverseLeftWords(s, k)