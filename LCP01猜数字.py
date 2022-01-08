#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/7 21:12
# @Author  : feifeigao
# @File    : LCP01猜数字.py
"""

#问题就是求两个列表的交集,思路错误，需要对应元素相等
# def game(guess, answer):
    # ret1= list(set(guess) & set(answer))
    # print(ret1)
    # return len(ret1)
#两个列表对应元素是否相等
def game(guess, answer):
    # 思路两个列表对应元素是否相等
    # 注 两个列表的交集,思路错误，需要对应元素相等;zip(a,b)用法
    count = 0
    for i, j in zip(guess, answer):
        # print(i,j)
        if i == j:
            count += 1
    return count


if __name__ == '__main__':
    guess = [1, 2, 3]
    answer = [1, 2, 3]
    guess = [2, 2, 3]
    answer = [3, 2, 1]
    r=game(guess, answer)

    print(r)
"""
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 打包为元组的列表
[(1, 4), (2, 5), (3, 6)]
>>> zip(a,c)              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
>>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]
"""