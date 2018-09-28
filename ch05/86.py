"""
86. 二叉查找树迭代器
设计实现一个带有下列属性的二叉查找树的迭代器：

元素按照递增的顺序被访问（比如中序遍历）
next()和hasNext()的询问操作要求均摊时间复杂度是O(1)
样例
对于下列二叉查找树，使用迭代器进行中序遍历的结果为 
[1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
挑战
额外空间复杂度是O(h)，其中h是这棵树的高度

Super Star：使用O(1)的额外空间复杂度
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

"""
方法一：通用解法
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root is not None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n is not None:
                self.stack.append(n)
                n = n.left
        
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        
        return node



"""
方法二：最简解法
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.curt = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return self.curt is not None or len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left
        
        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt
        