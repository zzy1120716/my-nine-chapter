"""
900. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, 
find the value in the BST that is closest to the target.

样例
Given root = {1}, target = 4.428571, return 1.

注意事项
Given target value is a floating point.
You are guaranteed to have only one unique value in the 
BST that is closest to the target.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
方法一：递归
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return 0
        
        lowerNode = self.lowerBound(root, target)
        upperNode = self.upperBound(root, target)
        
        if lowerNode is None:
            return upperNode.val
        
        if upperNode is None:
            return lowerNode.val
            
        if (target - lowerNode.val > upperNode.val - target):
            return upperNode.val
        
        return lowerNode.val
    
    
    def lowerBound(self, root, target):
        if root is None:
            return None
        
        if target <= root.val:
            return self.lowerBound(root.left, target)
        
        # target > root.val
        lowerNode = self.lowerBound(root.right, target)
        if lowerNode is not None:
            return lowerNode
        
        return root
        
        
    def upperBound(self, root, target):
        if root is None:
            return None
        
        if target > root.val:
            return self.upperBound(root.right, target)
        
        # target <= root.val
        upperNode = self.upperBound(root.left, target)
        if upperNode is not None:
            return upperNode
        
        return root


"""
方法二：非递归
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return 0
        
        lowerNode = self.lowerBound(root, target)
        upperNode = self.upperBound(root, target)
        
        if lowerNode is None:
            return upperNode.val
        
        if upperNode is None:
            return lowerNode.val
            
        if (target - lowerNode.val > upperNode.val - target):
            return upperNode.val
        
        return lowerNode.val
    
    
    def lowerBound(self, root, target):
        curr = root
        last = None
        while curr:
            if curr.val <= target:
                last = curr
                curr = curr.right
            else:
                curr = curr.left
        return last
        
        
    def upperBound(self, root, target):
        curr = root
        last = None
        while curr:
            if curr.val > target:
                last = curr
                curr = curr.left
            else:
                curr = curr.right
        return last