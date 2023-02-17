from . import *


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            vals.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        vals.sort(reverse=False)

        min_ = vals[-1] - vals[0]

        for i in range(len(vals) - 1):
            min_ = min(min_, vals[i], vals[i + 1])

        return min_
