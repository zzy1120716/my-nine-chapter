"""
114. 不同的路径
有一个机器人的位于一个 m × n 个网格左上角。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。

问有多少条不同的路径？

样例
给出 m = 3 和 n = 3, 返回 6.
给出 m = 4 和 n = 5, 返回 35.

注意事项
n和m均不超过100
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(m):
            for j in range(1, n):
                dp[j] = dp[j - 1] + dp[j]
        return dp[n - 1]

"""
stage1：unoptimized，时间O(n ^ 2)，空间O(m * n)
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        path = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[m - 1][n - 1]

"""
stage2：空间O(2min(m, n))
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m > n:
            return self.uniquePaths(n, m)
        pre = cur = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                cur[i] = cur[i - 1] + pre[i]
            pre, cur = cur, pre
        return pre[m - 1]

"""
stage3：空间O(min(m, n))
"""
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if m > n:
            return self.uniquePaths(n, m)
        cur = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                cur[i] += cur[i - 1]
        return cur[m - 1]