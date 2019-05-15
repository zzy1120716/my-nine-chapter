"""
475. 二叉树的最大路径和 II
给一棵二叉树，找出从根节点出发的路径中，和最大的一条。

这条路径可以在任何二叉树中的节点结束，但是必须包含至少一个点（也就是根了）。

样例
给出如下的二叉树：

  1
 / \
2   3
返回4。(最大的路径为1→3)
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
from collections import deque


# 方法一：分治法
class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        max_sum = self.helper(root)
        return max_sum

    def helper(self, root):
        if not root:
            return -sys.maxsize

        left = self.helper(root.left)
        right = self.helper(root.right)

        return root.val + max(0, max(left, right))


# 方法二：DFS，保存遍历过程中所有路径和，作为候选结果，最后返回最大值
class Solution1:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        vals = []
        self.dfs(root, 0, vals)
        return max(vals)

    def dfs(self, node, path_sum, vals):
        path_sum += node.val
        vals.append(path_sum)
        if node.left:
            self.dfs(node.left, path_sum, vals)
        if node.right:
            self.dfs(node.right, path_sum, vals)


# 方法三：BFS
class Solution2:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        # write your code here
        q = deque([(root, root.val)])
        ans = float('-inf')
        while q:
            cur = q.popleft()
            if cur[1] > ans:
                ans = cur[1]
            if cur[0].left:
                q.append((cur[0].left, cur[1] + cur[0].left.val))
            if cur[0].right:
                q.append((cur[0].right, cur[1] + cur[0].right.val))
        return ans
