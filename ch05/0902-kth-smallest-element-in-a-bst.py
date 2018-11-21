"""
902. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest
 to find the kth smallest element in it.

样例
Given root = {1,#,2}, k = 2, return 2.

挑战
What if the BST is modified (insert/delete operations)
 often and you need to find the kth smallest frequently?
  How would you optimize the kthSmallest routine?

注意事项
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        for i in range(k - 1):
            if not stack:
                break
            if stack[-1].right:
                node = stack[-1].right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
        
        return stack[-1].val
