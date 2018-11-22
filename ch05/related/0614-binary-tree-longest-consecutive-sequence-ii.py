"""
614. 二叉树的最长连续子序列 II
给定一棵二叉树，找到最长连续序列路径的长度。
路径起点跟终点可以为二叉树的任意节点。

样例
    1
   / \
  2   0
 /
3
返回 4 // 0-1-2-3
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

"""
这道题利用回溯的思想比较容易，因为当一个结点没有子结点时，它只需要跟其父结点进行比较，
这种情况最容易处理，而且一旦叶结点处理完了，我们可以一层一层的回溯，直到回到根结点，然后
再遍历的过程中不断的更新结果res即可。由于题目中说了要么是递增，要么是递减，我们不能一会
递增一会递减，所以我们递增递减的情况都要统计，只是最后取最长的路径。所以我们要知道每一个
结点的最长递增和递减路径的长度，当然是从叶结点算起，这样才方便往根结点回溯。当某个结点比
其父结点值大1的话，说明这条路径是递增的，那么当我们知道其左右子结点各自的递增路径长度，
那么当前结点的递增路径长度就是左右子结点递增路径长度中的较大值加上1，同理如果是递减路径，
那么当前结点的递减路径长度就是左右子结点递减路径长度中的较大值加上1，通过这种方式我们可以
更新每个结点的递增递减路径长度。在回溯的过程中，一旦我们知道了某个结点的左右子结点的最长
递增递减路径长度，那么我们可以算出当前结点的最长连续序列的长度，要么是左子结点的递增路径
跟右子结点的递减路径之和加1，要么是左子结点的递减路径跟右子结点的递增路径之和加1，二者中
取较大值即可。
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        left_len, left_down, left_up = self.helper(root.left)
        right_len, right_down, right_up = self.helper(root.right)

        down, up = 0, 0

        if root.left and root.left.val + 1 == root.val:
            down = max(down, left_down + 1)

        if root.left and root.left.val - 1 == root.val:
            up = max(up, left_up + 1)

        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down + 1)

        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up + 1)

        length = max(down + 1 + up, left_len, right_len)

        return length, down, up


class Solution1:

    def __init__(self):
        self.length = 1

    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        self.search(root)
        return self.length

    def search(self, root):
        if not root:
            return 0, 0

        up_length = down_length = 1

        left_up_len, left_down_len = self.search(root.left)
        right_up_len, right_down_len = self.search(root.right)

        if root.left:
            if root.left.val == root.val + 1:
                up_length = max(up_length, left_up_len + 1)
            if root.left.val == root.val - 1:
                down_length = max(down_length, left_down_len + 1)
        if root.right:
            if root.right.val == root.val + 1:
                up_length = max(up_length, right_up_len + 1)
            if root.right.val == root.val - 1:
                down_length = max(down_length, right_down_len + 1)

        self.length = max(self.length, up_length + down_length - 1)
        return up_length, down_length