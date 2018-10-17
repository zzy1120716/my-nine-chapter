"""
109. 数字三角形
给定一个数字三角形，找到从顶部到底部的最小路径和。
每一步可以移动到下面一行的相邻数字上。

样例
比如，给出下列数字三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

注意事项
如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，
其中n是数字三角形的总行数。
"""

"""
方法一：自底向上
"""
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        minpath = triangle[-1]
        for layer in range(n - 2, -1, -1):  # 对每一层
            for i in range(layer + 1):  # 检查层中的每个节点
                # 找到它的两个子节点中较小的一个，并将三角形中的当前值与它相加
                minpath[i] = min(minpath[i], minpath[i + 1]) + triangle[layer][i]
        return minpath[0]


"""
方法二：自顶向下
"""
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1])