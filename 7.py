#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/12 21:33
# @Author  : feifeigao
# @File    : 7.py
"""
"""
7: 整数反转
[题意]
x = 123
返回321

x=120
返回21
[思路题解]
将数字转字符串后进行倒置，最终再转换会int

[解题步骤]

[经典代码模板]

[tips]

[注意]
整数超过 32 位的有符号整数的范围 [−2 ^ 31, 2 ^ 31− 1] ，就返回 0

"""
def reverse(x):
    #符号校验
    sign=1
    if x<0:
        x=abs(x)
        sign=-1
    #反转字符串
    y=int(str(x)[::-1])*sign
    if -2**31<= y <= 2 **31-1:
        return y
    else:
        return 0


if __name__ == '__main__':
    nums=123
    nums=120
    nums=-120
    r=reverse(nums)
    print(r)

