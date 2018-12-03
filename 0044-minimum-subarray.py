"""
44. 最小子数组
给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

样例
给出数组[1, -1, -2, 1]，返回 -3

注意事项
子数组最少包含一个数字
"""


# DP
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        n = len(nums)
        dp = [nums[0]] + [0] * (n - 1)
        min_sum = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + (0 if dp[i - 1] > 0 else dp[i - 1])
            min_sum = min(min_sum, dp[i])
        return min_sum


# prefix sum
class Solution1:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # prefix sum: p[k] = nums[0] + nums[1] + ...+ nums[k]
        # prefix min subarray sum from k to 0: p[k] - max(p[k-1],p[k-2,...,p[1], p[0]]) for k = 1 ~ n-1
        # p[0] = nums[0] - 0

        if not nums or len(nums) == 0:
            return 0

        max_sum = 0
        min_sum = float('inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            min_sum = min(min_sum, total - max_sum)
            max_sum = max(max_sum, total)

        return min_sum