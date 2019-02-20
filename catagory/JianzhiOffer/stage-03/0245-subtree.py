"""
245. 子树
中文English
有两个不同大小的二叉树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

样例
下面的例子中 T2 是 T1 的子树：

       1                3
      / \              /
T1 = 2   3      T2 =  4
        /
       4
下面的例子中 T2 不是 T1 的子树：

       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4
注意事项
若 T1 中存在从节点 n 开始的子树与 T2 相同，我们称 T2 是 T1 的子树。
也就是说，如果在 T1 节点 n 处将树砍断，砍断的部分将与 T2 完全相同。
"""


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        if not T2:
            return True
        if not T1:
            return False

        if T1.val == T2.val and self.compare(T1, T2):
            return True
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def compare(self, s, t):
        if not s:
            return t is None
        if not t or s.val != t.val:
            return False
        return self.compare(s.left, t.left) and self.compare(s.right, t.right)


# 转化为字符串
class Solution2:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def get(self, root, rt):
        if root is None:
            rt.append("#")
            return

        rt.append(str(root.val))
        self.get(root.left, rt)
        self.get(root.right, rt)

    def isSubtree(self, T1, T2):
        # write your code here
        rt = []
        self.get(T1, rt)
        t1 = ','.join(rt)

        rt = []
        self.get(T2, rt)
        t2 = ','.join(rt)

        return t1.find(t2) != -1
