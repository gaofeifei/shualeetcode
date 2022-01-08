#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2021/12/13 23:30
# @Author  : feifeigao
# @File    : 27.py
"""
def fun27(nums,val):
    #我的
    # for i,v in enumerate(nums):
    #     if val==v:
    #         nums.pop(nums[i])
    #     # print(v)
    # print(nums)
    # print(len(nums))
    # return len(nums)

    #别人的
    # i = 0
    # while i < len(nums):
    #     if nums[i] != val:
    #         i += 1
    #     else:
    #         nums.remove(nums[i])
    # print(nums)
    # print(len(nums))
    # return i

    # 我的改进版
    #去重，不行呀
    # nums=set(nums)
    # print(nums)
    # 排序，不行呀
    nums=sorted(nums)
    print(nums)
    for i,v in enumerate(nums):
        if v==val:
            nums.remove(v)
    print(nums)
    print(len(nums))
    # return len(nums)
if __name__ == '__main__':
    # nums=[3,2,2,3]
    # nums =[0, 0, 1]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]#为啥最后这个没删掉呢？
    # 因为相邻的相同元素移除前一个之后，
    # 索引变了
    # nums=[0, 1, 2,7,2, 3, 0, 4, 2]
    fun27(nums,2)
