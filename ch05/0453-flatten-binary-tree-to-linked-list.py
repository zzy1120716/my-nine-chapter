"""
453. 将二叉树拆成链表
将一棵二叉树按照前序遍历拆解成为一个假链表。所谓的假链表是说，用
二叉树的 right 指针，来表示链表中的 next 指针。

样例
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
挑战
不使用额外的空间耗费。

注意事项
不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
方法一：分治法
"""
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.helper(root)
        
    
    # restructure and return last node in preorder
    def helper(self, root):
        if root is None:
            return None
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        if right_last is not None:
            return right_last
        
        if left_last is not None:
            return left_last
        
        return root


"""
方法二
"""
class Solution:
    last_node = None
    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
        
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)