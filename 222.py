#!/usr/bin/env/python3
# coding:utf-8
"""
# @Time    : 2022/1/11 16:33
# @Author  : feifeigao
# @File    : 222.py
"""
"""
222:完全二叉树的节点个数
[题意]
已知 完全二叉树的根节点 root ，求出该树的节点个数。
完全二叉树 定义：
在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。

[思路题解]
非空节点数=左子树+右子树+根结点

[解题步骤]

[经典代码模板]

[tips]

[注意]


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def a(root):
    #root根节点为空则节点数为0
    if root.right ==None and root.left==None and root.val==0:
        return 0
    else:
        print(root.left)
        return a(root.left)+a(root.right)+1

if __name__ == '__main__':
    root = TreeNode()
    # root = [1, 2, 3, 4, 5, 6]
    r=a(root)
    print(r)

