
#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2021/12/14 20:28
# @Author  : feifeigao
# @File    : 203.py
"""
import collections
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements203(head, val):
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    while head!=None and head.next!=None:
        if head.next==val:
            pre.next=head.next
            head=head.next
        else:
            pre=head
            head=head.next
    print(dummy.next)
    return dummy.next



if __name__ == '__main__':
    head=ListNode()
    hnext=head.next
    dq=collections.deque([1, 2, 6, 3, 4, 5, 6])
    # head = [1, 2, 6, 3, 4, 5, 6]
    # print(type(head))
    #用队列实现链表
    while len(dq)!=0:
        temp=dq.popleft()
        hnext=temp

    # val = 6
    # removeElements203(head, val)