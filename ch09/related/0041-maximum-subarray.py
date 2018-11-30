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
import sys


# 深入理解DP方法：
# 显然，这是一个优化问题，通常可以由DP解决。 因此，当谈到DP时，我们要弄清楚的第一件事是子问题的格式
# （或每个子问题的状态）。 当我们试图提出递归关系时，子问题的格式会很有用。
# 首先，我认为子问题应该是这样的：maxSubArray(nums, i, j)，这意味着nums[i:j]的maxSubArray。
# 通过这种方式，我们的目标是找出maxSubArray(nums, 0, len(nums)-1)是什么。 但是，如果我们以这种方式
# 定义子问题的格式，很难找到从子问题到原始问题的连接（至少对我而言）。 换句话说，我找不到将原始问题
# 划分为子问题的方法，并使用子问题的解决方案以某种方式创建原始问题的解决方案。
#
# 所以我将子问题的格式改为：maxSubArray(nums, i)，这意味着nums[0:i]的maxSubArray必须有nums[i]作为结束元素。
# 请注意，现在子问题的格式不像前一个格式那样灵活且功能不强，因为nums[i]应该包含在该序列中，我们必须跟踪子问题
# 的每个解以更新全局最优值。 但是，现在子问题和原始问题之间的联系变得更加清晰：
# maxSubArray(nums, i) = maxSubArray(nums, i - 1) if maxSubArray(nums, i - 1) > 0 else 0 + nums[i]
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        # dp[i] means the maximum subarray ending with nums[i]
        dp = [nums[0]] + [0] * (n - 1)
        maximum = dp[0]

        for i in range(1, n):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            maximum = max(maximum, dp[i])

        return maximum


# 方法二：分治法
class Solution1:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left > right:
            return -sys.maxsize
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        L = self.helper(nums, left, mid - 1)
        R = self.helper(nums, mid + 1, right)
        left_sum, tmp = 0, 0
        for i in range(mid - 1, left - 1, -1):
            tmp += nums[i]
            if tmp > left_sum:
                left_sum = tmp
        right_sum, tmp = 0, 0
        for i in range(mid + 1, right + 1):
            tmp += nums[i]
            if tmp > right_sum:
                right_sum = tmp
        return max(max(L, R), left_sum + right_sum + nums[mid])


if __name__ == '__main__':
    # 6
    print(Solution1().maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
    print(Solution1().maxSubArray([1, 3, -1, 2, -1, 2]))
