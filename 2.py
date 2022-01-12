#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 11:53
# @Author  : feifeigao
# @File    : 2.py
"""
"""
divmod()
返回一个包含商和余数的元组(a // b, a % b)
divmod(7, 2)
结果(3, 1)

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def a(l1,l2):
    count = 0
    # 实例链表
    ret = ListNode()
    tmp = ret
    while l1 or l2 or count:  # l1或l2或不为空
        num = 0
        if l1:  # 累加值
            num += l1.val
            l1 = l1.next
        if l2:
            num += l2.val
            l2 = l2.next
        if count:  # 累加 进位后count-1
            num += count
            count -= 1
        # 计算 被除数，10是除数 进位
        # count,num各赋值为商,余数
        count, num = divmod(num, 10)
        tmp.next = ListNode(num)
        tmp = tmp.next
    return ret.next


if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    l1,l2=ListNode(0),ListNode(0)
    r=a(l1,l2)
    print(r)

