#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/14 19:28
# @Author  : feifeigao
# @File    : 1636.py
"""
"""
1636:按照频率将数组升序排序
[题意]
将数组按照每个值的频率 升序 排序。
如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。
[思路题解]
2有3个，1有2个，统计好的[(2, 3), (1, 2), (3, 1)]结果。
按值升序排序，如果值相同按key降序排序

[解题步骤]

[经典代码模板]

[tips]

[注意]


"""
from collections import Counter
def a(nums):
    n=len(nums)
    c=Counter(nums)
    # print(c)
    # print(c.most_common())
    # print(c.items())
    # for val, count in c.most_common():
        # print(type(val))
        # print(val,count)
    # for x in nums:
        #统计x元素有几个
        # print(x,nums.count(x))
    print(nums)
    # 按照频率将数组升序排序
    #方法1
    l_asc=sorted(nums, key=lambda x: (nums.count(x), -x))
    l_asc1 = sorted(nums, key=lambda x: (nums.count(x), x))
    l_asc.reverse()
    print(l_asc)
    print(l_asc1)
    # begin
    # 方法2
    l_asc2=sorted(c.items(),key=lambda item:item[1])#由小到大 升
    # l_asc5 = sorted(c.items(), key=lambda item: item[1],reverse=True)#由大到小 降

    # print(l_asc2)
    # print(l_asc5)
    res2=[]
    for key, value in l_asc2:
        # print(key,value)
        res2.append([key]*value)
    total2 = res2[0]
    for i in range(1, len(res2)):
        total2 += res2[i]
    # print(total2)

    # end

    #按照频率将数组降序排序
    #begin
    s = sorted(c.items(), key=lambda item: item[1], reverse=True)
    res = []
    for key, value in s:
        # print(key,value)
        res.append([key]*value)#追加多个相同的值到列表
    total = res[0]
    for i in range(1, len(res)):
        total += res[i]
    # print(total)
    total.reverse()
    # print(total)
    #end
    return total




if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3,6,6]
    # nums = [2, 3, 1, 3, 2]
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    nums=[1, 5, 0, 5] #结果为：[1,0,5,5]
    a(nums)

