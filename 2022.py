#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/9 19:07
# @Author  : feifeigao
# @File    : 2022.py
"""
"""
2022. 将一维数组转变成二维数组


"""
def a(nums,m,n):
    t=len(nums)
    #m,n表示行列
    if m*n!=t:return []
    l2=[]
    for i in range(m):
        print(i)
        l2.append(nums[n*i:n*i+n])
    return l2


if __name__ == '__main__':
    nums= [1,2,3,4]
    m = 2
    n = 2
    nums =[1, 2]
    m = 1
    n = 1
    s=a(nums,m,n)

    nums =[3]
    m = 1
    n = 2
    print(s)
