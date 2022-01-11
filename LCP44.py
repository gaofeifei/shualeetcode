#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 17:07
# @Author  : feifeigao
# @File    : LCP44.py
"""
"""
LCP44:开幕式焰火
[题意]
统计二叉树不重复子节点个数
[思路题解]
遍历二叉树，用set去重，返回集合set的大小
DFS用递归的写法
[解题步骤]

[经典代码模板]

[tips]

[注意]


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def numColor(root):
    s=set([])
    def dfs(a):
        if not a :return
        dfs(a.left)
        dfs(a.right)
        s.add(a.val)
    dfs(root)
    return len(s)


if __name__ == '__main__':
    root=TreeNode()
    root=[1, 3, 2, 1, None, 2]
    r=numColor(root)
    print(r)
