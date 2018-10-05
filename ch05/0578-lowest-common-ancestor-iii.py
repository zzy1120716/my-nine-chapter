"""
578. 最近公共祖先 III
给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。

两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），
离这两个节点最近的公共的节点。

返回 null 如果两个节点在这棵树上不存在最近公共祖先的话。

样例
给出下面这棵树：

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

注意事项
这两个节点未必都在这棵树上出现。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

"""
方法一：分治法
"""
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)

        a = left_a or right_a or root == A
        b = left_b or right_b or root == B

        if root == A or root == B:
            return a, b, root

        if left_node is not None and right_node is not None:
            return a, b, root
        if left_node is not None:
            return a, b, left_node
        if right_node is not None:
            return a, b, right_node

        return a, b, None

"""
方法二：DFS，寻找到A和B的路径
"""
class Solution:
    route_a, route_b, temp = [], [], []

    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.dfs(root, A, B, self.temp)
        if self.route_a == [] or self.route_b == []:
            return None
        self.temp.reverse()
        self.route_a.reverse()
        self.route_b.reverse()
        for item in self.temp:
            if item.val in self.route_b and item.val in self.route_a:
                return item

    def dfs(self, root, A, B, temp):
        if root is None:
            return
        temp.append(root)
        if root.val == A.val:
            self.route_a = [item.val for item in temp]
        if root.val == B.val:
            self.route_b = [item.val for item in temp]
        if self.route_a != [] and self.route_b != []:
            return
        self.dfs(root.left, A, B, temp)
        self.dfs(root.right, A, B, temp)
        if self.route_a == [] or self.route_b == []:
            temp.pop()