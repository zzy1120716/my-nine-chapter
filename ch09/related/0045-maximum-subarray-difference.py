"""
45. 最大子数组差
给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

样例
给出数组[1, 2, -3, 1]，返回 6

挑战
时间复杂度为O(n)，空间复杂度为O(n)

注意事项
子数组最少包含一个数
"""
import sys


# 和 Maximum Subarray II 的思路是一样的，只不过那题求的是两个 subarray 的和的最大值，这里求的是差的最大值。
#
# 1. 顺序找到每个位置 i 左边（包括 i）的 subarray 的 max sum & min sum
# 2. 逆序找到每个位置 i 右边（包括 i）的 subarray 的 max sum & min sum
# 3. 枚举两个 subarray 的分割线位置（范围 [0, n-1]），最大差为 max(顺序max - 逆序min，顺序min - 逆序 max)
#
# 技巧：
# 复用 Maximum Subarray 的代码，找 minimum subarray 就把原数组每个数取负再传进去（返回的结果再取负回来），
# 找逆序的 maximum subarray 就把原数组反过来传进去（返回的结果再反回来）。
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        # 分别找顺序、逆序的max&min
        left_max = self._maximum_subarray(nums)
        right_max = self._maximum_subarray(nums[::-1])[::-1]

        left_min = self._maximum_subarray(self._negate_array(nums))
        left_min = self._negate_array(left_min)
        right_min = self._maximum_subarray(self._negate_array(nums)[::-1])[::-1]
        right_min = self._negate_array(right_min)

        # 枚举分割线的位置
        max_diff = - sys.maxsize - 1
        for i in range(len(nums) - 1):
            max_diff = max(max_diff,
                           abs(left_max[i] - right_min[i + 1]),
                           abs(left_min[i] - right_max[i + 1]))
        return max_diff

    def _negate_array(self, nums):
        return list(map(lambda x: -x, nums))

    def _maximum_subarray(self, nums):
        max_sum = - sys.maxsize - 1
        max_sums = []
        prev_min_sum = 0
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            max_sum = max(max_sum, curr_sum - prev_min_sum)
            max_sums.append(max_sum)
            prev_min_sum = min(prev_min_sum, curr_sum)

        return max_sums