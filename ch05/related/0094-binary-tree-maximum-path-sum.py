"""
94. 二叉树中的最大路径和
给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束
（路径和为两个节点之间所在路径上的节点权值之和）

样例
给出一棵二叉树：

       1
      / \
     2   3
返回 6
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        max_sum, _ = self.helper(root)
        return max_sum

    def helper(self, root):
        if not root:
            return -sys.maxsize, 0

        left_max_path, left_single_path = self.helper(root.left)
        right_max_path, right_single_path = self.helper(root.right)

        max_path = max(left_max_path, right_max_path, root.val + left_single_path + right_single_path)
        single_path = max(left_single_path + root.val, right_single_path + root.val, 0)

        return max_path, single_path
