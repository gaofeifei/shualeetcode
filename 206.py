#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2021/12/14 23:24
# @Author  : feifeigao
# @File    : 206.py
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList206(head: ListNode):
    dummy=ListNode(0)#实例头结点
    dummy.next=head#指向head指向的结点
    while head != None and head.next != None:
        dnext=dummy.next#声明下个结点值
        hnext=head.next
        #图 第1步(1)
        dummy.next=hnext
        #图 第2步(2)
        head.next=hnext.next
        #图 第3步(3)
        hnext.next=dnext
    return dummy.next
