#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/29 9:23
# @Author  : feifeigao
# @File    : 29-老是超时.py
"""
"""
29-老是超时:
[题意]

[思路题解]
除法就是做减法并将其所做减法次数累加
老是超时怎办，做溢出判断
[解题步骤]

[经典代码模板]

[tips]

[注意]


"""
def dividel(dividend,divisor):
    MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
    flag = 1  # 存储正负号，并将分子分母转化为正数
    if dividend < 0: flag, dividend = -flag, -dividend
    if divisor < 0: flag, divisor = -flag, -divisor

    res = 0
    while dividend >= divisor:  # 例：1023 / 1 = 512 + 256 + 128 + 64 + 32 + 16 + 8 + 4 + 1
        cur = divisor
        multiple = 1
        while cur + cur < dividend:  # 用加法求出保证divisor * multiple <= dividend的最大multiple
            cur += cur  # 即cur分别乘以1, 2, 4, 8, 16...2^n，即二进制搜索
            multiple += multiple
        dividend -= cur
        res += multiple

    res = res if flag > 0 else -res  # 恢复正负号

    # 根据是否溢出返回结果
    if res < MIN_INT:
        return MIN_INT
    elif MIN_INT <= res <= MAX_INT:
        return res
    else:
        return MAX_INT



if __name__ == '__main__':
    a, b = 10, 3
    a, b = -2147483648, -1
    a, b = 2147483647, 1
    a, b = -2147483648, 1
    c=dividel(a, b)


