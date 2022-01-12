#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 16:18
# @Author  : feifeigao
# @File    : 4.py
"""
""""""
def a(nums1,nums2):
    nums1.extend(nums2)
    nums1.sort()
    n=len(nums1)
    res=0
    # print(n)
    if n==0 or n is None:return 0
    if n==1:return nums1[0]/1.0000
    if n%2==0:
        print(nums1[n // 2-1])
        print(nums1[n // 2 ])
        res = (nums1[n // 2-1] + nums1[n // 2]) / 2.0000
    else:
        res = nums1[n//2]/1.0000
    print(res)
    return res


if __name__ == '__main__':
    nums= [1,2,3]
    nums1 = [1, 3]
    nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3,4]
    r=a(nums1,nums2)
    # print(r)
