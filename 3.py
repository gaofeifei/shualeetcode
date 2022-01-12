#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 12:01
# @Author  : feifeigao
# @File    : 3.py
"""
#3. 无重复字符的最长子串
#给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

def lengthOfLongestSubstring(s):
    cur,res=[],0
    for i in range(len(s)):
        while s[i] in cur:
            cur.pop(0)#列表滑动窗口，右边进左边出
        cur.append(s[i])#右侧无论如何都会进入新的
        res=max(len(cur),res)
    return res

if __name__ == '__main__':
    # s = "abcabcbb"
    # s = "bbbbb"
    s = "pwwkew"
    # s = ""
    r=lengthOfLongestSubstring(s)
    print(r)

