#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 22:27
# @Author  : feifeigao
# @File    : 1122.py
"""
"""
1122:
[题意]

[思路题解]


[解题步骤]

[经典代码模板]

[tips]

[注意]

"""
from collections import Counter
def a(arr1,arr2):
    d1=dict()
    for i,k in enumerate(arr2):
        # print(i,k)
        d1[k] = i
    #     print(d1[k])
    # print(d1)
    # arr1.sort(key=lambda x: ((0, d1[x]) if x in d1 else (1, x)))

    #如果arr1的元素在d1里 记录0，否则记录1
    # 第一个排序准则是x是否在arr2中，如果在则key = 0，先排，
    # 否则key = 1，后排，第二个排序准则是在arr2中的下标或者x本身的大小
    # 自定义排序
    print(lambda x:(0, d1[x]) if x in d1 else (1, x))
    # print(arr1)
    return arr1





if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    a(arr1,arr2)

