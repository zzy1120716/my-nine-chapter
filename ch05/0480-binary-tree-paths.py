"""
480. 二叉树的所有路径
给一棵二叉树，找出从根节点到叶子节点的所有路径。

样例
给出下面这棵二叉树：

   1
 /   \
2     3
 \
  5
所有根到叶子的路径为：

[
  "1->2->5",
  "1->3"
]
"""


# 方法一：基于Traverse的DFS
class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
            
        res = []
        self.helper(root, [], res)
        return res

    def helper(self, node, path, res):
        path.append(str(node.val))
        
        if node.left is None and node.right is None:
            res.append('->'.join(path))
            path.pop()
            return
        
        if node.left:
            self.helper(node.left, path, res)
        
        if node.right:
            self.helper(node.right, path, res)
        
        path.pop()


# 方法二：基于Divide & Conquer的DFS
class Solution1:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
        
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
        
        return paths


# 方法三：另一种Traversal
class Solution2:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        
        res = []
        self.dfs(root, [str(root.val)], res)
        return res

    def dfs(self, node, path, res):
        if node.left is None and node.right is None:
            res.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, res)
            path.pop()
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, res)
            path.pop()
