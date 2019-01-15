"""
85. 在二叉查找树中插入节点
给定一棵二叉查找树和一个新的树节点，将节点插入到树中。

你需要保证该树仍然是一棵二叉查找树。

样例
给出如下一棵二叉查找树，在插入节点6之后这棵二叉查找树可以是这样的：

  2             2
 / \           / \
1   4   -->   1   4
   /             / \
  3             3   6
挑战
能否不使用递归？

注意事项
保证不会出现重复的值
"""


# 方法一：递归
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        if node.val < root.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)
        return root


# 方法二：非递归
class Solution1:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node

        curr = root
        while curr != node:
            if node.val < curr.val:
                if not curr.left:
                    curr.left = node
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                curr = curr.right
        return root
