"""
272. 爬楼梯 II
一个小孩爬一个 n 层台阶的楼梯。他可以每次跳 1 步， 2 步 或者 3 步。
实现一个方法来统计总共有多少种不同的方式爬到最顶层的台阶。

样例
n = 3
1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3

返回 4.
"""


# 动态规划，思路同 #111 爬楼梯 I
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 1:
            return 1
        if n == 2:
            return 2

        a, b, c = 1, 1, 2
        for i in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


class Solution1:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        return dp[n]


class Solution2:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n + 1):
            for j in range(1, 4):
                if i >= j:
                    f[i] += f[i - j]
        return f[n]