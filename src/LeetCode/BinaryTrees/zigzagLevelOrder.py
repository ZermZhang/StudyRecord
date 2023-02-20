from . import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}

        def bfs(curr: Optional[TreeNode] = root, level: int = 0):
            nonlocal res
            if not curr:
                return
            if level % 2 == 1:
                if level not in res:
                    res[level] = [curr.val]
                else:
                    res[level].insert(0, curr.val)
            else:
                if level not in res:
                    res[level] = [curr.val]
                else:
                    res[level].append(curr.val)
            bfs(curr=curr.left, level=level + 1)
            bfs(curr=curr.right, level=level+1)
        
        bfs()
        return res.values()
