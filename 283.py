#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2021/12/13 22:41
# @Author  : feifeigao
# @File    : 283.py
"""
def fun283(nums):

    for i,v in enumerate(nums):
        if 0==v:
            nums.remove(0)
            nums.append(0)
    print(nums)


if __name__ == '__main__':
    nums=[0,1,0,3,12]
    # nums =[0, 0, 1]
    fun283(nums)
