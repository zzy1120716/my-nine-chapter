"""
68. 二叉树的后序遍历
给出一棵二叉树，返回其节点值的后序遍历。

样例
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [3,2,1]

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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.helper(root.right)
        self.result.append(root.val)


# 非递归
"""
利用两个栈
https://www.youtube.com/watch?v=qT65HltK2uE
"""
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if not root:
            return result

        s1, s2 = [], []
        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        while s2:
            result.append(s2.pop().val)

        return result


"""
在实现遍历的循环中维持一种不变的关系：
1. 栈中结点序列的左边是二叉树已遍历过的部分，右边是尚未遍历的部分
2. 如果curNode不空，其父结点就是栈顶结点
3. curNode空时，栈顶就是应访问的结点
根据被访问结点是其父结点的左子结点或右子结点，就可以决定下一步怎么做：如果是左子结点就
转到右兄弟；如果是右子结点，就应该处理根结点并强制退栈。
"""
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        stack = []

        curr = root
        while stack or curr:
            # 能左就左，否则向右一步
            while curr:
                stack.append(curr)
                curr = curr.left if curr.left else curr.right

            # pop stack，添加到结果
            curr = stack.pop()
            result.append(curr.val)

            # 栈不空且当前节点是栈顶的左子节点，转到其右兄弟，否则退栈
            if stack and stack[-1].left == curr:
                curr = stack[-1].right
            else:
                curr = None

        return result