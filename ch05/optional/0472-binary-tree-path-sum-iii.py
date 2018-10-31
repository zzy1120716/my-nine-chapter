"""
472. 二叉树的路径和 III
给一棵二叉树和一个目标值，找到二叉树上所有的和为该目标值的路径。路径可以从二叉树的
任意节点出发，任意节点结束。

样例
给一棵这样的二叉树：

    1
   / \
  2   3
 /
4
和目标值 target = 6。你需要返回的结果为：

[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]
"""

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


# 官方答案
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, results)
        return results

    def dfs(self, root, target, results):
        if not root:
            return

        path = []
        self.find_sum(root, None, target, path, results)

        self.dfs(root.left, target, results)
        self.dfs(root.right, target, results)

    def find_sum(self, root, father, target, path, results):
        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(path[:])

        if root.parent not in [None, father]:
            self.find_sum(root.parent, root, target, path, results)

        if root.left not in [None, father]:
            self.find_sum(root.left, root, target, path, results)

        if root.right not in [None, father]:
            self.find_sum(root.right, root, target, path, results)

        path.pop()


# 遍历每个节点，以每个节点为起始，做DFS，找出所有符合的组合
class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []

        # inorder traverse
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left

            # for each node, do dfs to find all valid paths
            curr = stack.pop()
            self.dfs(None, curr, target, [], results)

            curr = curr.right

        return results

    def dfs(self, prev, node, target, path, results):
        target -= node.val
        path.append(node.val)

        if target == 0:
            results.append(path[:])

        if node.left and node.left != prev:
            self.dfs(node, node.left, target, path, results)

        if node.right and node.right != prev:
            self.dfs(node, node.right, target, path, results)

        if node.parent and node.parent != prev:
            self.dfs(node, node.parent, target, path, results)

        # backtracking
        path.pop()