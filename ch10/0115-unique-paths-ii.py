"""
115. 不同的路径 II
114"不同的路径" 的跟进问题：

现在考虑网格中有障碍物，那样将会有多少条不同的路径？

网格中的障碍和空位置分别用 1 和 0 来表示。

样例
如下所示在3x3的网格中有一个障碍物：

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
一共有2条不同的路径从左上角到右下角。

注意事项
m 和 n 均不超过100
"""

"""
stage 1
"""
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]

"""
stage 2
"""
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        pre = cur = [0] * m

        for i in range(m):
            if not obstacleGrid[i][0]:
                pre[i] = 1
            else:
                break

        for j in range(1, n):
            flag = False
            if not obstacleGrid[0][j]:
                cur[0] = pre[0]
                if cur[0]:
                    flag = True
            else:
                cur[0] = 0
            for i in range(1, m):
                if not obstacleGrid[i][j]:
                    cur[i] = cur[i - 1] + pre[i]
                    if cur[i]:
                        flag = True
                else:
                    cur[i] = 0
            if not flag:
                return 0
            pre, cur = cur, pre

        return pre[m - 1]

"""
stage 3
"""
class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * m
        for i in range(0, m):
            if not obstacleGrid[i][0]:
                cur[i] = 1
            else:
                break

        for j in range(1, n):
            flag = False
            if obstacleGrid[0][j]:
                cur[0] = 0
            else:
                flag = True
            for i in range(1, m):
                if not obstacleGrid[i][j]:
                    cur[i] += cur[i - 1]
                    if cur[i]:
                        flag = True
                else:
                    cur[i] = 0
            if not flag:
                return 0

        return cur[m - 1]