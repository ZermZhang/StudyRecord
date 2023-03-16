#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : buildTree
@Software       : PyCharm
@Modify Time    : 2023/3/16 08:31
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from . import *


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:])
        return root
