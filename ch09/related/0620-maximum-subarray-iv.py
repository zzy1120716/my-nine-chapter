"""
620. 最大子序列的和IV
给定一个整数数组，找到长度大于或等于 k 的连续子序列使它们的和最大，返回这个最大的和，
如果数组中少于k个元素则返回 0

样例
给定一个数组为 [-2,2,-3,4,-1,2,1,-5,3]，k = 5，连续的子序列为 [2,-3,4,-1,2,1] 时有最大和
sum = 5

注意事项
确保返回结果为整型
"""


class Solution:
    """
    @param nums: an array of integer
    @param k: an integer
    @return: the largest sum
    """
    def maxSubarray4(self, nums, k):
        # write your code here
        n = len(nums)
        if n < k:
            return 0

        result = 0
        for i in range(k):
            result += nums[i]

        pre_sum = [0 for _ in range(n + 1)]

        min_prefix = 0
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            if i >= k and pre_sum[i] - min_prefix > result:
                result = max(result, pre_sum[i] - min_prefix)

            if i >= k:
                min_prefix = min(min_prefix, pre_sum[i - k + 1])

        return result


if __name__ == '__main__':
    print(Solution().maxSubarray4([-2, 2, -3, 4, -1, 2, 1, -5, 3], 5))
