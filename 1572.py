#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/8 18:23
# @Author  : feifeigao
# @File    : 1572.py
"""
"""
1572. 矩阵对角线元素的和
https://leetcode-cn.com/problems/matrix-diagonal-sum/
"""

#a方法失败[[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]不通过
def a(nums):
    n=len(nums)
    col=len(nums[0])
    print(n,col)
    i=0
    j=0
    sums_p=0#主对角线
    sums_s=0#副对角线
    ji=0
    while True:
        if i >= n and j >= col: break
        # print(nums[i][j])
        sums_p+=nums[i][j]
        sums_s+=nums[n-i-1][col-i-1]
        i+=1
        j+=1
    # print(sums_p)
    print(sums_s)
    # print(sums_p+sums_s)
    if n % 2 != 0:  # 奇数行列
        ji = nums[n // 2][col // 2]
        return sums_p + sums_s - ji
    return sums_p+sums_s

def b(nums):
    n = len(nums)
    ans=0
    for i in range(n):
        # print(nums[i][i])
        ans+=nums[i][i]
        # print(ans)
        #将主对角线的值清零
        nums[i][i]=0
        #继续累加副对角线的值，不会有重复的，因为清零了
        ans+=nums[i][n-i-1]
    return ans

if __name__ == '__main__':
    # nums = [[1,2,3],
    #         [4,5,6],
    #         [7,8,9]]
    # nums = [[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
    # nums= [[5]]
    nums=[[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
    r=b(nums)
    print(r)

