"""
901. Closest Binary Permutation Tree Value II
Given a non-empty binary search tree and a target value,
 find k values in the BST that are closest to the target.

样例
Given root = {1}, target = 0.000000, k = 1, return [1].

挑战
Assume that the BST is balanced, could you solve it in 
less than O(n) runtime (where n = total nodes)?

注意事项
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values 
in the BST that are closest to the target.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 方法一：暴力法，中序遍历二叉树，在数组中找最接近target的k个数。
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        values = []
        
        self.traverse(root, values)
        i, tmp, n = 0, 0, len(values)
        for i in range(n):
            if values[i] >= target:
                break
        
        if i >= n:
            return values[n - k : n]
            
        left, right = i - 1, i
        result = []
        for i in range(k):
            if left >= 0 and (right >= n or target - values[left] < values[right] - target):
                result.append(values[left])
                left -= 1
            else:
                result.append(values[right])
                right += 1
        
        return result

    def traverse(self, root, values):
        if root is None:
            return
        self.traverse(root.left, values)
        values.append(root.val)
        self.traverse(root.right,values)


# 方法二：左右扩展（最优），把树当做数组，move_upper当做i+=1，move_lower当做i-=1
class Solution1:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        values = []
        
        if k == 0 or not root:
            return values
            
        low_s = self.get_stack(root, target)
        up_s = low_s[:]
        # find the closest index
        if target < low_s[-1].val:
            self.move_lower(low_s)
        else:
            self.move_upper(up_s)
        # then move to prev or next node
        for i in range(k):
            if not low_s or (up_s and target - low_s[-1].val > up_s[-1].val - target):
                values.append(up_s[-1].val)
                self.move_upper(up_s)
            else:
                values.append(low_s[-1].val)
                self.move_lower(low_s)
        
        return values
    
    def get_stack(self, root, target):
        stack = []
        while root is not None:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return stack
    
    # get the prev node
    def move_lower(self, low_s):
        n = low_s[-1]
        if not n.left:
            n = low_s.pop()
            while low_s and low_s[-1].left == n:
                n = low_s.pop()
            return
        n = n.left
        while n is not None:
            low_s.append(n)
            n = n.right
    
    # get the next node
    def move_upper(self, up_s):
        n = up_s[-1]
        if not n.right:
            n = up_s.pop()
            while up_s and up_s[-1].right == n:
                n = up_s.pop()
            return
        n = n.right
        while n is not None:
            up_s.append(n)
            n = n.left
