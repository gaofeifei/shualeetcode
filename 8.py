#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/12 22:42
# @Author  : feifeigao
# @File    : 8.py
"""
"""
8:字符串转换整数 (atoi)
[题意]
字符串转换成整数,将字符中含有的数字转换成整型
[思路题解]


[解题步骤]

[经典代码模板]

[tips]
i.isdigit()
ret += i 构成字符串
[注意]


"""
def myAtoi(s):
    negative = None
    ret = ''
    new_s = s.strip()
    # print(s)
    #空串校验
    if not new_s:
        return 0
    #负数校验
    if new_s[0] == '-':
        negative = True
        new_s = new_s[1:]
    #英文字母（大写和小写）、' '、'+'、'-' 和 '.' 校验
    #只返回数字
    for i in new_s:
        if negative is None and i == '+':
            negative = False
        #是否是数字，数字提取
        elif i.isdigit():
            ret += i
        #其他情况退出
        else:
            break
    #返回结果不合法
    if not ret:
        return 0
    #转换成整型
    ret = int(ret)
    #负数，返回[-2^31, 2^31 - 1]范围中 最大的负数max(ret, -2 ** 31)
    if negative:
        ret = -ret
        return max(ret, -2 ** 31)
    #正数，返回最小的min(2 ** 31 - 1, ret)
    return min(2 ** 31 - 1, ret)

if __name__ == '__main__':
    s= " -123*4"
    r=myAtoi(s)
    print(r)

