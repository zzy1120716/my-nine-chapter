"""
66. 二叉树的前序遍历
给出一棵二叉树，返回其节点值的前序遍历。

样例
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
 返回 [1,2,3].

挑战
你能使用非递归实现么？
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 递归
class Solution:

    result = []

    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.helper(root.left)
        self.helper(root.right)


"""
非递归
1. 有点类似BFS的写法，只不过是用stack而不是queue：
2. 首先把root入栈
3. 出栈的元素同时放进结果队列
4. 先把右儿子节点入栈，再把左儿子节点入栈，这样出栈的顺序是先左后右（根节点已出）
按照这个次序继续，直到stack为空
"""
class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result