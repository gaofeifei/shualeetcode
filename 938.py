#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 21:16
# @Author  : feifeigao
# @File    : 938.py
"""
"""
938:二叉搜索树的范围和
[题意]
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和
[思路题解]
先排序，再根据范围要求找到对应值相加

[解题步骤]

[经典代码模板]

[tips]
二叉树的中序遍历是从小到大排序
[注意]

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
    cur = 0
    def dfs(node):
        nonlocal cur
        if node.left:
            dfs(node.left)
        if node.val > high:
            return
        if node.val >= low:
            cur+=node.val
        if node.right:
            dfs(node.right)
    dfs(root)
    return cur

if __name__ == '__main__':
    root = [10,5,15,3,7,13,18,1,None,6]
    root=TreeNode()
    low = 6
    high = 10
    r=rangeSumBST(root,low,high)
    print(r)

