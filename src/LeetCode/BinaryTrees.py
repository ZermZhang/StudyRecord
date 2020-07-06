#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : BinaryTrees.py
@Software       : PyCharm
@Modify Time    : 7/6 22:00     
@Author         : zermelzhang
@version        : 1.0
@Desciption     : the leetcode problem about BinaryTrees
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def get_minimum_difference(root: TreeNode) -> int:
        res, prev = float("inf"), float("-inf")

        def dfs(root):
            nonlocal res, prev  # 将变量标记为自有变量
            if not root:
                return
            dfs(root.left)  # 遍历左子树
            res = min(res, root.val - prev)     # 计算当前节点和前面节点的差
            prev = root.val
            dfs(root.right)  # 遍历右子树

        dfs(root)
        return res