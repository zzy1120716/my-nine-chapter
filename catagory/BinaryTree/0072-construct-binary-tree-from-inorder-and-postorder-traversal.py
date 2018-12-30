"""
72. 中序遍历和后序遍历树构造二叉树
根据中序遍历和后序遍历树构造二叉树

样例
给出树的中序遍历： [1,2,3] 和后序遍历： [1,3,2]

返回如下的树：

  2

 /  \

1    3

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
    def buildTree(self, inorder, postorder):
        # write your code here
        if not inorder:
            return
        root = TreeNode(postorder[-1])
        root_pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:root_pos], postorder[:root_pos])
        root.right = self.buildTree(inorder[root_pos + 1:], postorder[root_pos:-1])
        return root


if __name__ == '__main__':
    print(Solution().buildTree([1, 2, 3], [1, 3, 2]))
