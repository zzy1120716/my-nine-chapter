"""
43. 最大子数组 III
给定一个整数数组和一个整数 k，找出 k 个不重叠子数组使得它们的和最大。
每个子数组的数字在数组中的位置应该是连续的。

返回最大的和。

样例
给出数组 [-1,4,-2,3,-2,3] 以及 k = 2，返回 8

注意事项
子数组最少包含一个数
"""
import sys


# dp[i][j] represent i numbers, k subarrays which has largest sum1
# 1.我们大家一般平常写的dp方程式如下，不实用于这道题。
# 这样的方程式并不能解决sum类的问题。
# 因为每次j + 1的过程中，我们只考虑了加一个数，而不是多个数
# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i])
#
# 2.要解决好这道题，我们必须考虑简历两个dp:localMaX 和 globalMax
# localMaX可以被用来解决加多个数的问题，即最后一个数是否在整个sum的计算里
# localMaX[i][j] represent the maxSUM
#             when it has i subarrays, j number
#             and the last number nums[k - 1] is included
#             
# globalMax[i][j] represent the maxSUM
#             when it has i subarrays, j number
#             and the last number nums[k - 1] is included or not included
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        localMaX = [[0 for i in range(n + 1)] for j in range(k + 1)]
        globalMax = [[0 for i in range(n + 1)] for j in range(k + 1)]

        for i in range(1, k + 1):
            # 当 k = 0 时候，sum 肯定是 = 0
            # 当 k > 0 而数字个数 < k 则是 -sys.maxsize， 因为根本无法执行
            # 由于一直要从左取，所以这个 -sys.maxsize（无法执行）是可以传递的
            # 所以只要声明一次即可
            localMaX[i][0] = -sys.maxsize
            globalMax[i][0] = -sys.maxsize
            for j in range(1, n + 1):
                # localMax 无非就是 多 +了一个 nums[j - 1] 只要列举能加上nums[j - 1]的情况即可
                localMaX[i][j] = max(globalMax[i - 1][j - 1] + nums[j - 1], localMaX[i][j - 1] + nums[j - 1])
                # gobolMax 没有限制条件，所以对local 取max即可
                globalMax[i][j] = max(localMaX[i][j], globalMax[i][j - 1])

        return globalMax[-1][-1]