"""
595. 二叉树最长连续序列
给一棵二叉树，找到最长连续路径的长度。
这条路径是指 任何的节点序列中的起始节点到树中的任一节点都必须遵循 父-子 联系。
最长的连续路径必须是从父亲节点到孩子节点（不能逆序）。

样例
举个例子：

   1
    \
     3
    / \
   2   4
        \
         5
最长的连续路径为 3-4-5，所以返回 3。

   2
    \
     3
    /
   2
  /
 1
最长的连续路径为 2-3 ,而不是 3-2-1 ，所以返回 2。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 方法一
class Solution:

    def __init__(self):
        self.length = 0

    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.helper(root, 1)
        return self.length

    def helper(self, root, path_len):
        if not root:
            return

        if root.left:
            if root.left.val == root.val + 1:
                self.helper(root.left, path_len + 1)
            else:
                self.helper(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.helper(root.right, path_len + 1)
            else:
                self.helper(root.right, 1)

        self.length = max(self.length, path_len)


# 官方答案1
class Solution1:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root, None, 0)

    def helper(self, root, parent, length_without_root):
        if not root:
            return 0

        length = length_without_root + 1 if parent and parent.val + 1 == root.val else 1
        left = self.helper(root.left, root, length)
        right = self.helper(root.right, root, length)
        return max(length, max(left, right))


# 官方答案2
class Solution2:

    def __init__(self):
        self.longest = 0

    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.helper(root)
        return self.longest

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        subtree_longest = 1  # at least we have root
        if root.left and root.val + 1 == root.left.val:
            subtree_longest = max(subtree_longest, left + 1)
        if root.right and root.val + 1 == root.right.val:
            subtree_longest = max(subtree_longest, right + 1)

        self.longest = max(self.longest, subtree_longest)
        return subtree_longest


# 官方答案3：分治法，多个返回值Java版本需要class ResultType
class Solution3:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return 0, 0

        left_max_in_subtree, left_max_from_root = self.helper(root.left)
        right_max_in_subtree, right_max_from_root = self.helper(root.right)

        # is the root itself
        max_in_subtree, max_from_root = 0, 1

        if root.left and root.val + 1 == root.left.val:
            max_from_root = max(max_from_root, left_max_from_root + 1)

        if root.right and root.val + 1 == root.right.val:
            max_from_root = max(max_from_root, right_max_from_root + 1)

        max_in_subtree = max(max_from_root, max(left_max_in_subtree, right_max_in_subtree))
        return max_in_subtree, max_from_root


# 方法二：记录可能的path
# 不直接得到 length， 而是先记录每个符合条件的 length 都有哪些点，
# 然后计算这些 length 的size，能够得到更加完整的结果。
import sys


class Solution4:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.result = []
        temp = []
        length = -sys.maxsize
        self.findconsecutive(root, temp)

        for n in self.result:
            if len(n) > length:
                length = len(n)

        return length

    def findconsecutive(self, root, temp):

        if root is None:
            return None

        temp.append(root.val)

        # if root.left is None and root.right is None:
        self.result.append(temp.copy())

        if root.left is not None:
            if root.left.val - 1 == root.val:
                self.findconsecutive(root.left, temp)
                temp.pop()
            else:
                self.findconsecutive(root.left, [])

        if root.right is not None:
            if root.right.val - 1 == root.val:
                self.findconsecutive(root.right, temp)
                temp.pop()
            else:
                self.findconsecutive(root.right, [])