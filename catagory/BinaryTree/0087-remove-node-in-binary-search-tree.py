"""
87. 删除二叉查找树的节点
给定一棵具有不同节点值的二叉查找树，删除树中与给定值相同的节点。如果树中没有相同值的节点，
就不做任何处理。你应该保证处理之后的树仍是二叉查找树。

样例
给出如下二叉查找树：
          5
        /   \
       3     6
      / \
     2   4
删除节点3之后，你可以返回：
          5
        /  \
      2     6
      \
       4
或者：
          5
       /    \
     4       6
   /
 2
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Best Solution
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # null case
        if root is None:
            return root

        # check if node to delete is in left/right subtree
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            # if root is has 2 childs/only one child/leaf node
            if root.left and root.right:
                max = self.findMax(root)
                root.val = max.val
                root.left = self.removeNode(root.left, max.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None

        return root

    # find max node in left subtree of root
    def findMax(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node


# 方法一：分治法
class Solution1:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if not root:
            return root
        if value < root.val:
            root.left = self.removeNode(root.left, value)
            return root
        if value > root.val:
            root.right = self.removeNode(root.right, value)
            return root
        # 开始执行删除操作
        # 1. 删除根节点
        if not root.left and not root.right:
            root = None
            return root
        # 2(1). 只有一个child，只有右子树
        if not root.left and root.right:
            root = root.right
            return root
        # 2(2). 只有一个child，只有左子树
        if not root.right and root.left:
            root = root.left
            return root
        # 3. 有两个child
        if root.left and root.right:
            # 挑选左子树中最大的或者右子树中最小的，替换当前节点，再将替换的节点置空
            max_in_left = self.findMaxInLeftTree(root.left)
            root.val = max_in_left
            root.left = self.removeNode(root.left, max_in_left)
            return root
        return root

    # 找到左子树中的最大值
    def findMaxInLeftTree(self, left):
        if not left:
            return 0
        if not left.right:
            return left.val
        if not left.left and not left.right:
            return left.val
        return self.findMaxInLeftTree(left.right)


# 方法二：
# 中序遍历二叉树，将遍历结果保存在list中（除去值为value的节点），再构造二叉查找树。
class Solution2:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ans = []

    def inorder(self, root, value):
        if root is None:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, l, r):
        if l == r:
            node = TreeNode(self.ans[l])
            return node

        if l > r:
            return None

        mid = (l + r) // 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node

    def removeNode(self, root, value):
        # write your code here
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)
