"""
563. 背包问题 V
给出 n 个物品, 以及一个数组, nums[i] 代表第i个物品的大小, 保证大小均为正数并且没有重复,
正整数 target 表示背包的大小, 找到能填满背包的方案数。
每一个物品只能使用一次

样例
给出候选物品集合 [1,2,3,3,7] 以及 target 7

结果的集合为:
[7]
[1,3,3]
返回 2
"""


# 方法一：n ^ 2 解法，TLE
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        n = len(nums)
        m = target
        if not n:
            return 0

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 0

        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(m + 1):
                dp[i][j] = dp[i - 1][j]

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]


# 方法二
class Solution1:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        dp = [0] * (target + 1)
        dp[0] = 1

        for a in nums:
            for j in range(target, a - 1, -1):
                dp[j] += dp[j - a]

        return dp[-1]


# 方法三：滚动数组 + prefix sum
class Solution2:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        f = [[0] * (target + 1), [0] * (target + 1)]
        f[0][0] = 1
        n = len(nums)
        prefix_sum = 0
        for i in range(1, n + 1):
            f[i % 2][0] = 1
            prefix_sum += nums[i - 1]
            for j in range(1, min(target, prefix_sum) + 1):
                f[i % 2][j] = f[(i - 1) % 2][j]
                if j >= nums[i - 1]:
                    f[i % 2][j] += f[(i - 1) % 2][j - nums[i - 1]]

        return f[n % 2][target]


if __name__ == '__main__':
    print(Solution1().backPackV([1, 2, 3, 3, 7], 7))
