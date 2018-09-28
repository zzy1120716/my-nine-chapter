"""
596. 最小子树
给一棵二叉树, 找到和为最小的子树, 返回其根节点。

样例
给一棵二叉树：

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
返回节点 1

注意事项
LintCode会打印根节点为你返回节点的子树。保证只有
一棵和最小的子树并且给出的二叉树不是一棵空树。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
方法一：纯Divide & Conquer
"""
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        minimum, subtree, sum = self.helper(root)
        return subtree
    
    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0
        
        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)
        
        sum = left_sum + right_sum + root.val
        
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum
        
        return sum, root, sum

"""
方法二：Divide Conquer + Traverse
"""
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.minimum_weight = sys.maxsize
        self.result = None
        self.helper(root)
        
        return self.result
    
    def helper(self, root):
        if root is None:
            return 0
        
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)
        
        if left_weight + right_weight + root.val <= self.minimum_weight:
            self.minimum_weight = left_weight + right_weight + root.val
            self.result = root
        
        return left_weight + right_weight + root.val