"""
448. 二叉查找树的中序后继
给定一个二叉查找树(什么是二叉查找树)，以及一个节点，求该节点在中序遍历的后继，
如果没有返回null

样例
给出 tree = [2,1] node = 1:

  2
 /
1
返回 node 2.

给出 tree = [2,1,3] node = 2:

  2
 / \
1   3
返回 node 3.

挑战
O(h)，其中h是BST的高度。

注意事项
保证p是给定二叉树中的一个节点。(您可以直接通过内存地址找到p)
"""

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


# 递归
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root:
            return

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root


# 非递归
class Solution1:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root and p.val != root.val:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if not root:
            return None

        if not root.right:
            return successor

        root = root.right
        while root.left:
            root = root.left

        return root


# 非递归简化版
class Solution2:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
