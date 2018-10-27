"""
70. 二叉树的层次遍历 II
给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）

样例
给出一棵二叉树 {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
按照从下往上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
"""

"""
方法一：层次遍历直接reverse（同#69，略）
"""

"""
方法二：思路是 dfs，在遍历时往 ans 塞入空数组，同时保存这个节点的索引和深度
最后遍历一次 preorder，按照对应坑位塞节点
"""
class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        result = []
        if not root:
            return result

        preorder = [(root, 1)]
        self.dfs(root, result, preorder, 0)

        # 不能在dfs中做append
        # 因为最深的节点可能是右子节点
        height = len(result)
        for node, level in preorder:
            result[height - level].append(node.val)

        return result

    def dfs(self, node, result, preorder, parent_at):
        if len(result) < preorder[parent_at][1]:
            result.append([])

        depth = preorder[parent_at][1] + 1

        if node.left:
            preorder.append((node.left, depth))
            self.dfs(node.left, result, preorder, len(preorder) - 1)

        if node.right:
            preorder.append((node.right, depth))
            self.dfs(node.right, result, preorder, len(preorder) - 1)