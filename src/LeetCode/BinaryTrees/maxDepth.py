from . import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def dfs(root: Optional[TreeNode], depth: int) -> Optional[int]:
            if not root:
                return depth
            depth = depth + 1
            return max(dfs(root.left, depth), dfs(root.right, depth))

        return dfs(root=root, depth=depth)

    def maxDepth_v2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth_v2(root.left), self.maxDepth_v2(root.right))