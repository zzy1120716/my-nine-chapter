"""
619. 二叉树的最长连续子序列III
这题是 二叉树的最长连续子序列II 的后续。
给出一棵 k叉树，找到最长连续序列路径的长度.
路径的开头跟结尾可以是树的任意节点。

样例
一个样例如下：k叉树 5<6<7<>,5<>,8<>>,4<3<>,5<>,3<>>>，表示如下结构:

     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 3

返回 5, // 3-4-5-6-7
"""
"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # write your code here
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        max_len, down, up = 0, 0, 0

        for child in root.children:
            max_len_tmp, max_down, max_up = self.helper(child)
            max_len = max(max_len, max_len_tmp)
            if child.val + 1 == root.val:
                down = max(down, max_down + 1)
            if child.val - 1 == root.val:
                up = max(up, max_up + 1)

        max_len = max(max_len, down + 1 + up)

        return max_len, down, up