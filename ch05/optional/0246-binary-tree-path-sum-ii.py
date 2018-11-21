"""
246. 二叉树的路径和 II
给一棵二叉树和一个目标值，设计一个算法找到二叉树上的和为该目标值的所有路径。
路径可以从任何节点出发和结束，但是需要是一条一直往下走的路线。也就是说，路
径上的节点的层级是逐个递增的。

样例
对于二叉树：

    1
   / \
  2   3
 /   /
4   2
给定目标值6。那么满足条件的路径有两条：

[
  [2, 4],
  [1, 3, 2]
]
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        result = []
        path = []
        if not root:
            return result
        self.dfs(root, path, result, 0, target)
        return result

    def dfs(self, root, path, result, level, target):
        if not root:
            return
        path.append(root.val)
        tmp = target
        for i in range(level, -1, -1):
            tmp -= path[i]
            if tmp == 0:
                result.append(path[i:])

        self.dfs(root.left, path, result, level + 1, target)
        self.dfs(root.right, path, result, level + 1, target)

        path.pop()


# DFS2
class Solution1:

    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        result = []
        if root:
            self.helper(root, target, [], result)
        return result

    def helper(self, root, target, path, result):
        if not root:
            return
        path.append(root.val)
        cur_sum = 0
        for i in range(len(path) - 1, -1, -1):
            cur_sum += path[i]
            if cur_sum == target:
                result.append(path[i:])

        self.helper(root.left, target, path, result)
        self.helper(root.right, target, path, result)

        path.pop()


# 先序遍历 + 回溯法，通用模板
class Solution2:

    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        result = []
        if not root:
            return result
        path = []
        path.append(root.val)
        self.dfs(root, target, path, result)
        return result

    def dfs(self, root, target, path, result):
        if not root:
            return
        cur_sum = 0
        for i in range(len(path) - 1, -1, -1):
            cur_sum += path[i]
            if cur_sum == target:
                result.append(path[i:])

        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, target, path, result)
            path.pop()

        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, target, path, result)
            path.pop()