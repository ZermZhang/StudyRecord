from . import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}

        def bfs(curr: Optional[TreeNode] = root, level: int = 0):
            # 注意二叉树操作过程中的常见逻辑
            # 二叉树操作主要分成两种：BFS，DFS
            # 区别在于具体的操作和递归操作左右子节点的位置
            # 针对二叉树的最大区别打过集中在具体操作上，剩余的左右子树基本都可以通过递归完成操作
            nonlocal res
            # 二叉树遍历最后都会遍历到空的叶子节点上，所以一定要有一个返回空节点的过程
            if not curr:
                return
            # 记录当前比例的是那一层的结果
            if level % 2 == 1:
                # 奇数层使用栈对该层的每个节点的值进行记录
                # 因为后续的遍历过程是先遍历左子树、再遍历右子树
                # 所以这里需要从头开始插入val
                if level not in res:
                    res[level] = [curr.val]
                else:
                    res[level].insert(0, curr.val)
            else:
                # 和上一个条件的处理逻辑相反
                if level not in res:
                    res[level] = [curr.val]
                else:
                    res[level].append(curr.val)
            # 对左子树进行相同的遍历
            bfs(curr=curr.left, level=level + 1)
            # 对右子树进行相同的遍历
            bfs(curr=curr.right, level=level+1)
        
        bfs()
        return res.values()
