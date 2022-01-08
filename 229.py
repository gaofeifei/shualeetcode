#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/6 14:53
# @Author  : feifeigao
# @File    : 229.py
"""
from collections import Counter

def majorityElement(nums):
    # [16, 16, 16, 23, 23, 12, 12, 12]
    #元素16的值有3个，23的值有2个，12的值有3个
    #n表示元素，v表示容器中所含这个元素的个数 16有3个 n=16,v=3
    # print(Counter(nums).items())#dict_items([(16, 3), (23, 2), (12, 3)])

    #列表推导式，遍历统计结果
    # for n, v in Counter(nums).items():
    #     print(n, v)

    #如果元素个数大于数组长度的1/3，则返回对应的元素
    print([n for n, v in Counter(nums).items() if v > len(nums) // 3])
    # print(8//3)#2
if __name__ == '__main__':
    nums=[16,16,16,23,23,12,12,12]
    majorityElement(nums)