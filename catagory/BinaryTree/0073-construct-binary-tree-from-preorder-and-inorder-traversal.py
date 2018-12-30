"""
73. 前序遍历和中序遍历树构造二叉树
根据前序遍历和中序遍历树构造二叉树.

样例
给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:

  2
 / \
1   3
注意事项
你可以假设树中不存在相同数值的节点
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder:
            return
        root = TreeNode(preorder[0])
        root_pos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_pos + 1], inorder[:root_pos])
        root.right = self.buildTree(preorder[root_pos + 1:], inorder[root_pos + 1:])
        return root


if __name__ == '__main__':
    print(Solution().buildTree([1, 2, 3], [2, 1, 3]))
