#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File           : isCompleteTree
@Software       : PyCharm
@Modify Time    : 2023/3/15 09:03
@Author         : zermzhang
@version        : 1.0
@Desciption     :
"""
from . import *

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # 完全二叉树，从左到右，从上到下依次编号，中间没有空缺的二叉树
        queue = [root]
        node = root
        while queue:
            cur = queue.pop(0)
            if cur:
                if not node:
                    return False
                queue.append(cur.left)
                queue.append(cur.right)
            node = cur
        return True