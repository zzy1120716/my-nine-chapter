"""
155. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。
样例
给出一棵如下的二叉树:

        1

     /     \

   2       3

          /    \

        4      5

这个二叉树的最小深度为 2
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 官方答案
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0

        left, right = 0, 0
        if node.left:
            left = self.dfs(node.left)
        else:
            return self.dfs(node.right) + 1

        if node.right:
            right = self.dfs(node.right)
        else:
            return self.dfs(node.left) + 1

        return min(left, right) + 1


# BFS：返回遇到的第一个叶子结点的层数即可
class Solution:

    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0

        from collections import deque
        queue = deque([root])
        min_depth = 0

        while queue:
            min_depth += 1
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if not curr.left and not curr.right:
                    return min_depth

        return min_depth