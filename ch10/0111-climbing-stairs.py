"""
111. 爬楼梯
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你
只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例
比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法

返回 3
"""


# 方法一：暴力法（超时）时间O(2 ^ n)，空间O(n)
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        return self.climb(0, n)

    def climb(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb(i + 1, n) + self.climb(i + 2, n)


# 方法二：带记忆的递归
class Solution1:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        memo = [0] * n
        return self.climb(0, n, memo)

    def climb(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb(i + 1, n, memo) + self.climb(i + 2, n, memo)
        return memo[i]


# 方法三：动态规划
class Solution2:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# 方法四：斐波那契数
class Solution3:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second


# 方法五：Binets Method
class Solution4:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        q = [[1, 1], [1, 0]]
        res = self.pow(q, n)
        return res[0][0]

    def pow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1 == 1:
                ret = self.multiply(ret, a)
            n >>= 1
            a = self.multiply(a, a)
        return ret

    def multiply(self, a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c


# 方法六：斐波那契公式
class Solution5:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 0:
            return 0
        import math
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(fibn / sqrt5)