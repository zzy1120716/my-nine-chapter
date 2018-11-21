"""

915. Inorder Predecessor in BST
Given a binary search tree and a node in it, find the in-order predecessor of that
node in the BST.

样例
Given root = {2,1,3}, p = 1, return null.

注意事项
If the given node has no in-order predecessor in the tree, return null
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 方法一：
# 利用BST的性质：往左走的时候不记,往右走的时候记
# 即保存即将向右拐的节点，当找到目标节点时，保存的节点就是中序遍历的前序节点
class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        predecessor = None

        while root:
            if p.val <= root.val:
                root = root.left
            else:
                predecessor = root
                root = root.right

        return predecessor


# 方法二：DFS
# 设计一个全局变量turn_right ，代表上一个有右拐的点，开始为None
# 然后如果是左拐，对这个变量不作处理，右拐的话，刷新这个全局变量为当前root
# 找到p,如果p有左子树，那么返回左子树，没有的话，就返回它前面上一个右拐的点
class Solution1:

    turn_right = None

    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        if not root:
            return

        if p.val > root.val:
            self.turn_right = root
            return self.inorderPredecessor(root.right, p)
        elif p.val < root.val:
            return self.inorderPredecessor(root.left, p)
        else:
            if root.left:
                return self.most_right(root.left)
            else:
                return self.turn_right

    def most_right(self, root):
        while root.right:
            root = root.right
        return root
