"""
88. Lowest Common Ancestor of a Binary Tree
给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。

最近公共祖先是两个节点的公共的祖先节点且具有最大深度。

样例
对于下面这棵二叉树

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7

注意事项
假设给出的两个节点都在树中存在
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 官方答案
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        """
        在root为根的二叉树中找A,B的LCA：
        如果找到了就返回这个LCA
        如果只碰到了A，就返回A
        如果只碰到了B，就返回B
        如果都没有，就返回None
        """
        if not root or root == A or root == B:
            return root

        # Divide
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        # Conquer
        # A 和 B 一边一个
        if left and right:
            return root

        # 左子树有一个点或者左子树有LCA
        if left:
            return left
        # 右子树有一个点或者右子树有LCA
        if right:
            return right

        # 左右子树啥都没有
        return None


# 先求从根节点到A，B各自的路径的方法
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        path_a = self.find_path(root, A)
        path_b = self.find_path(root, B)
        i, j = len(path_a) - 1, len(path_b) - 1
        while i >= 0 and j >= 0 and path_a[i] == path_b[j]:
            i -= 1
            j -= 1
        return path_a[i + 1]

    def find_path(self, root, target):
        path = []
        if not root:
            return path

        left_path = self.find_path(root.left, target)
        right_path = self.find_path(root.right, target)

        path.extend(left_path)
        path.extend(right_path)

        if len(path) != 0 or root == target:
            path.append(root)

        return path