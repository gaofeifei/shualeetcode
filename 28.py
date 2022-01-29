#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/26 5:18
# @Author  : feifeigao
# @File    : 28.py
"""
"""
28:
[题意]

[思路题解]
KMP 之所以能够在 O(m + n)O(m+n) 复杂度内完成查找，
是因为其能在「非完全匹配」的过程中提取到有效信息进行复用，以减少「重复匹配」的消耗。

[解题步骤]

[经典代码模板]
优化解法用KMP
https://www.zhihu.com/question/21923021/answer/281346746
[tips]

[注意]
当 needle 是空字符串时我们应当返回 0
超时，时间复杂度
"""
def strStr1(haystack,needle):
    n=len(needle)
    m=len(haystack)
    s,p=haystack, needle
    if n<=0 :return 0
    if m<=0 :return -1
    if needle not in haystack:return -1
    #暴力枚举 枚举haystack,needle的每个位置
    #再判断needle的每个字符是否和haystack里的字符匹配
    for i in range(m):
        for j in range(n):
            #判断是否匹配,不匹配，退出
            if s[i+j]!=p[j]: break
            #匹配：匹配到最后一个字符，说明可以完全匹配
            if j==n-1:return i
    #没找到匹配的
    return -1

#优化算法，避免无效枚举
# 暴力枚举中 重复的前缀(相同的字符)会 进行多次重复的匹配操作，直接影响效率
#优化点：怎么做才能不进行多次重复匹配操作，
#找到最长匹配的字符串(即使较后面的字符不一致，
# 但是找到了前面匹配的较长的字符，不必再反复比较他们，只需比较后面的字符)
def strStr(haystack,needle):
    lh = len(haystack)
    ln = len(needle)

    for i in range(lh - ln + 1):
        # 在haystack里找与needle相同的字符串
        if haystack[i:i + ln] == needle:
            return i
    else:#循环结束没有找到匹配位置
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    haystack = ""
    needle = ""
    haystack = ""
    needle = "a"
    r=strStr(haystack,needle)
    print(r)
