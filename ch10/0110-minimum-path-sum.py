"""
110. 最小路径和
给定一个只含非负整数的m*n网格，找到一条从
左上角到右下角的可以使数字和最小的路径。

注意事项
你在同一时间只能向下或者向右移动一步
"""

"""
stage 1
"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        sum = [[grid[0][0]] * n for _ in range(m)]
        for i in range(1, m):
            sum[i][0] = sum[i - 1][0] + grid[i][0]
        for j in range(1, n):
            sum[0][j] = sum[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = min(sum[i - 1][j], sum[i][j - 1]) + grid[i][j]
        return sum[m - 1][n - 1]


"""
stage 2
"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        pre, cur = [grid[0][0]] * m, [0] * m
        for i in range(1, m):
            pre[i] = pre[i - 1] + grid[i][0]
        for j in range(1, n):
            cur[0] = pre[0] + grid[0][j]
            for i in range(1, m):
                cur[i] = min(cur[i - 1], pre[i]) + grid[i][j]
            pre, cur = cur, pre
        return pre[m - 1]

"""
stage 3
"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m, n = len(grid), len(grid[0])
        cur = [grid[0][0]] * m
        for i in range(1, m):
            cur[i] = cur[i - 1] + grid[i][0]
        for j in range(1, n):
            cur[0] += grid[0][j]
            for i in range(1, m):
                cur[i] = min(cur[i - 1], cur[i]) + grid[i][j]
        return cur[m - 1]