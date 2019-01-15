"""
632. 二叉树的最大节点
在二叉树中寻找值最大的节点并返回。

样例
Example 1:
    Input:
     1
   /   \
 -5     3
 / \   /  \
1   2 -4  -5

    Output: The node with value 3.
    Explanation:
        return the node with max value.

Example 1:
    Input:
     10
   /   \
 -5     2
 / \   /  \
0   3 -4  -5

    Output: The node with value 10.
    Explanation:
        return the node with max value.

return the node with value 3.
"""
import sys


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# 层次遍历
class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if not root:
            return root

        max_value = -sys.maxsize
        max_node = None
        queue = [root]
        while queue:
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if curr.val > max_value:
                    max_value = curr.val
                    max_node = curr
        return max_node


# 先序遍历
class Solution1:

    def __init__(self):
        self.max_node = None

    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if not root:
            return root
        self.traverse(root)
        return self.max_node

    def traverse(self, root):
        if not root:
            return

        if not self.max_node or self.max_node.val < root.val:
            self.max_node = root

        if root.left:
            self.traverse(root.left)

        if root.right:
            self.traverse(root.right)


# 官方答案，分治法，需要定义比较TreeNode的方法
class Solution2:

    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # Write your code here
        if root is None:
            return root

        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        return b


if __name__ == '__main__':
    tn1 = TreeNode(1)
    tn2 = TreeNode(-5)
    tn3 = TreeNode(3)
    tn2.left = TreeNode(1)
    tn2.right = TreeNode(2)
    tn3.left = TreeNode(-4)
    tn3.right = TreeNode(-5)
    tn1.left = tn2
    tn1.right = tn3
    print(Solution().maxNode(tn1).val)
