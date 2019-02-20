"""
376. 二叉树的路径和
中文English
给定一个二叉树，找出所有路径中各节点相加总和等于给定 目标值 的路径。

一个有效的路径，指的是从根节点到叶节点的路径。

样例
给定一个二叉树，和 目标值 = 5:

     1
    / \
   2   4
  / \
 2   3
返回：

[
  [1, 2, 2],
  [1, 4]
]
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        ans = []
        self.helper(root, [], ans, target)
        return ans

    def helper(self, root, path, ans, target):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val == target:
            ans.append(path[:])
        self.helper(root.left, path, ans, target - root.val)
        self.helper(root.right, path, ans, target - root.val)
        path.pop()
