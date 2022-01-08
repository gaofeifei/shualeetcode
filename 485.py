#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2021/12/13 21:39
# @Author  : feifeigao
# @File    : 485.py
"""

def fun485(a):
    #list转string
    str1="".join((str(id) for id in a))
    #按0拆成子串数组
    substr=str1.split('0')
    #找出最大子串数组
    v=max(substr)
    #为了统计次数，转换成list
    v1=list(v)
    #map() 会根据提供的函数对指定序列做映射。
    #第一个参数 function 以参数序列中的每一个元素调用 function 函数，
    # 返回包含每次 function 函数返回值的新列表。
    #把list表中的每个元素都转换成int整型,最后转换成list
    vint=list(map(int, v1))
    #对列表求和
    vmax=sum(vint)
    print(vmax)


if __name__ == '__main__':
    a=[1,1,0,1,1,1]
    fun485(a)
