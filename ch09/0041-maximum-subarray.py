"""
41. 最大子数组
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。

样例
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6

挑战
要求时间复杂度为O(n)

注意事项
子数组最少包含一个数
"""

"""
方法一：前缀和
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum

"""
方法二：动态规划DP
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1]) + nums[i]
        max_value = - sys.maxsize - 1
        for v in dp:
            max_value = max(max_value, v)
        return max_value

"""
方法三：贪心greedy
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        sum = 0
        slice = - sys.maxsize - 1
        for n in nums:
            sum += n
            slice = max(slice, sum)
            sum = max(0, sum)
        return slice