"""
597. 具有最大平均数的子树
给一棵二叉树，找到有最大平均值的子树。返回子树的根结点。

样例
给一个二叉树：

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
返回节点 11。

注意事项
LintCode会打印出根结点为你返回节点的子树，保证有最大平均数子树只有一棵
"""

"""
DFS，分治法思想
利用二叉树的后序遍历进行递归
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:

    average, node = 0, None

    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if not root:
            return 0, 0

        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)

        tree_sum = left_sum + right_sum + root.val
        size = left_size + right_size + 1

        if not self.node or tree_sum / size > self.average:
            self.node = root
            self.average = tree_sum / size

        return tree_sum, size