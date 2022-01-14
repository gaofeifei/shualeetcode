#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/12 13:12
# @Author  : feifeigao
# @File    : 5.py
"""
"""
5:最长回文子串
[题意]
字符串 s，找到 s 中最长的回文子串。
回文串：正着读=反着读
输入：s = "babad"
输出："bab"
[思路题解]
用动态规划思想
写出动态规划的状态转移方程
    P(i,j)=P(i+1,j−1)∧(S i==S j)
也就是说，只有 s[i+1:j-1]是回文串，并且 s 的第 i 和 j 个字母相同时，s[i:j]才会是回文串。

[解题步骤]
回文子串只有两种情况：
奇数回文，即 aba
偶数回文，即 abba
那么我们只需要循环字符串的每一个index，当满足一下条件时，
从中心向两边扩展？？？
left >= 0
right < len(s)
s[left] == s[right] 对于第三个条件，存在奇数回文和偶数回文的判断：
奇数回文时，我们初始left == right
偶数回文时，我们初始化right == left + 1
根据这两种情况进行遍历，最终即可获取结果

[经典代码模板]

[tips]

[注意]

"""

def longestPalindrome(s):
    n=len(s)
    #边界判断 长度小于2都返回原字符串
    if n<2: return s
    res=''
    def find(left,right):
        nonlocal res
        #回文字符串满足的条件
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        res = s[left + 1:right] if right-left-1 > len(res) else res
        # print(res)
    for i in range(n):
        find(i,i)#奇数回文
        find(i,i+1)#偶数回文
    return res


if __name__ == '__main__':
    s = "babad"
    s = "cbbd"
    r=longestPalindrome(s)
    print(r)

