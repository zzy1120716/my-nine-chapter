"""
97. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。

样例
给出一棵如下的二叉树:

  1
 / \
2   3
   / \
  4   5
这个二叉树的最大深度为3.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# DFS模板
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.max_depth = 0
        self.dfs(root, 1)
        return self.max_depth

    def dfs(self, root, curr_depth):
        if not root:
            return
        self.max_depth = max(self.max_depth, curr_depth)
        self.dfs(root.left, curr_depth + 1)
        self.dfs(root.right, curr_depth + 1)


# 官方答案
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1