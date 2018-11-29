"""
584. 丢鸡蛋II
有一个n层的建筑。如果一个鸡蛋从第k层及以上落下，它会碎掉。如果从低于这一层的任意层落下，
都不会碎。
有m个鸡蛋，用最坏的情况下实验次数最少的方法去找到k, 返回最坏情况下所需的实验次数。

样例
给出 m = 2, n = 100 返回 14
给出 m = 2, n = 36 返回 8
"""
import sys


# 方法一：动态规划
class Solution:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, eggs, floors):
        # write your code here
        T = [[0] * (floors + 1) for _ in range(eggs + 1)]
        for i in range(floors + 1):
            T[1][i] = i

        for e in range(2, eggs + 1):
            for f in range(1, floors + 1):
                T[e][f] = sys.maxsize
                for k in range(1, f + 1):
                    c = 1 + max(T[e - 1][k - 1], T[e][f - k])
                    if c < T[e][f]:
                        T[e][f] = c

        return T[eggs][floors]


# 方法二：
# https://leetcode.com/articles/super-egg-drop/#
# Dynamic Programming with Optimality Criterion
class Solution1:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, K, N):
        # write your code here
        # Right now, dp[i] represents dp(1, i)
        dp = range(N+1)

        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > \
                                max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2

        return dp[-1]


# 方法三：DFS + Memoization, O(mn^2)
class Solution2:
    """
    @param m: the number of eggs
    @param n: the number of floors
    @return: the number of drops in the worst case
    """
    def dropEggs2(self, m, n):
        # write your code here
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.count(m, n, memo)

    def count(self, m, n, memo):
        if n == 0:
            return 0

        if m == 0:
            return -1

        if m == 1:
            return n

        if memo[m][n] != -1:
            return memo[m][n]

        min_drops = sys.maxsize
        for x in range(1, n + 1):
            break_drops = 1 + self.count(m - 1, x - 1, memo)
            not_break_drops = 1 + self.count(m, n - x, memo)
            min_drops = min(min_drops, max(break_drops, not_break_drops))

        memo[m][n] = min_drops
        return min_drops


if __name__ == '__main__':
    print(Solution1().dropEggs2(2, 100))  # 14
    print(Solution1().dropEggs2(2, 36))  # 8
