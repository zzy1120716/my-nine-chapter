"""
71. 二叉树的锯齿形层次遍历
给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）

样例
给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
返回其锯齿形的层次遍历为：

[
  [3],
  [20,9],
  [15,7]
]
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
方法一：层次遍历，用count记录行数，偶数层将该层序列翻转后append
"""
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if not root:
            return result

        from collections import deque
        queue = deque([root])
        count = 0

        while queue:
            count += 1
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if count % 2 == 1:
                result.append(level)
            else:
                result.append(level[::-1])

        return result


"""
方法二：前序遍历，记录每个节点所处的层数，
若为奇数层，则在list尾部插入；
若为偶数层，则在list头部插入
"""
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        self.result = []
        self.preorder(root, 0, self.result)
        return self.result

    def preorder(self, root, level, result):
        if root:
            if len(result) < level + 1:
                result.append([])
            if level % 2 == 0:
                result[level].append(root.val)
            else:
                result[level].insert(0, root.val)
            self.preorder(root.left, level + 1, result)
            self.preorder(root.right, level + 1, result)


"""
方法三：使用两个list
"""
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if not root:
            return result

        currLevel = [root]
        nextLevel = []
        normal_order = True

        while currLevel:
            level = []
            while currLevel:
                curr = currLevel.pop()
                level.append(curr.val)
                if normal_order:
                    if curr.left:
                        nextLevel.append(curr.left)
                    if curr.right:
                        nextLevel.append(curr.right)
                else:
                    if curr.right:
                        nextLevel.append(curr.right)
                    if curr.left:
                        nextLevel.append(curr.left)

            result.append(level)
            currLevel, nextLevel = nextLevel, currLevel
            normal_order = not normal_order

        return result