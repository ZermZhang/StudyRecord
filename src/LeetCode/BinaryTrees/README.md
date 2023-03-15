# 二叉树
> 二叉树是树形结构中的一个重要类型。许多实际问题都可以抽象成为二叉树的形式。
> 又因为二叉树的存储结构和算法相对较为简单，因此二叉树显得尤为重要。也是算法题目中极为常见的一个考点。

## 1. 二叉树结构
二叉树（binary tree）是指树中节点的度不大于2的有序树。
常见的二叉树有二叉树（binary tree），二叉搜索树（ordered binary tree），完全二叉树（completed binary tree），均衡二叉树（balanced binary tree）等。


## 2. 遍历算法

### 2.1 深度遍历
```python
def dfs(root):
    if not root:
        return None
    dfs(root.left)
    dfs(root.right)
    print(root.val)
```

### 2.2 广度遍历
```python
def bfs(root):
    if not root:
        return None
    print(root.val)
    bfs(root.left)
    bfs(root.right)
```
### 2.3 中央遍历
```python
def mfs(root):
    if not root:
        return None
    mfs(root.left)
    print(root.val)
    mfs(root.right)
```

## 3. 常用关联数据结构
### 3.1 队列、栈
> 队列和栈是在解决二叉树问题过程中常用的两种数据结构。
> 因为队列先进先出和栈先进后出的性质能够很好的保存二叉树遍历过程中的节点顺序信息，方便根据二叉树的遍历信息进行操作。

#### Eg. zigzagLevelOrder
该问题中，需要将二叉树的节点值按照拉链的方式往复输出，因此，在每一层里针对节点的便利方式是相反的。
为了解决这种问题，在解决方案中，引入了队栈的结构分别对奇数层和偶数层进行处理
![zigzagLevelOrder](https://raw.githubusercontent.com/ZermZhang/pictures/main/20230315092654.png)
```python
def zigzagLevelOrder(root):
    res = {}
    
    def bfs(curr, level):
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
        bfs(curr=curr.left, level=level+1)
        bfs(curr=curr.right, leve=level+1)
    
    bfs(root, 0)
    return res.values()
```
说明：
* 采用bfs，即广度遍历方法
  * 因为需要将每一层的节点值记录下来，广度遍历天然适合按照二叉树的每一层对各个节点进行处理
* 在bfs的处理过程中，传入level信息，记录当前是哪一层，根据层号来进行判断，当前层的节点顺序是该用队列处理还是该用栈处理
  * 偶数层，也就是从左到右进行数据读取的时候，使用队列，从list右边添加元素
  * 奇数层，也就是从右到左进行数据读取的时候，使用栈，从list左边添加元素
* 额外的，注意处理逻辑和左右递归bfs的顺序
  * 根据具体情况，处理逻辑可以在左右遍历之前、中间、之后三种情况
  * 一般情况下，需要对root节点进行处理的时候大多是采用中间的情况，具体情况具体分析