"""
69. 二叉树的层次遍历
给出一棵二叉树，返回其节点值的层次遍历
（逐层从左往右访问）

样例
给一棵二叉树 {3,9,20,#,#,15,7} ：

  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
挑战
挑战1：只使用一个队列去实现它

挑战2：用DFS算法来做
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        
        if not root:
            return result
        
        q = [root]
        
        while q:
            level = []
            size = len(q)
            for i in range(size):
                now = q[0]
                level.append(now.val)
                del q[0]
                if now.left:
                    q.append(now.left)
                if now.right:
                    q.append(now.right)
            result.append(level)
            
        return result


# 官方
# from lintcode import TreeNode
class Solution1:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return self.results
