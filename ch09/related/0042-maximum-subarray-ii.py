"""
42. 最大子数组 II
给定一个整数数组，找出两个 不重叠 子数组使得它们的和最大。
每个子数组的数字在数组中的位置应该是连续的。
返回最大的和。

样例
给出数组 [1, 3, -1, 2, -1, 2]
这两个子数组分别为 [1, 3] 和 [2, -1, 2] 或者 [1, 3, -1, 2] 和 [2]，它们的最大和都是 7

挑战
要求时间复杂度为 O(n)

注意事项
子数组最少包含一个数
"""
import sys


# 思路基于#41题，从左向右求left max subarray，从右向左求right max subarray，得到两个数组left和right，
# 找一个划分的点，使left和right下标相差为1的两个元素和最大。

# 方法一：Kadane's Algorithm
# https://mnmunknown.gitbooks.io/algorithm-notes/626,_dong_tai_gui_hua_ff0c_subarray_lei.html
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0

        n = len(nums)
        # Maximum subarray value from left/right with n elements
        left = [0] * n
        right = [0] * n

        left[0] = nums[0]
        prev_max = nums[0]
        maximum = nums[0]
        for i in range(1, n):
            prev_max = max(nums[i], nums[i] + prev_max)
            maximum = max(maximum, prev_max)

            left[i] = maximum

        right[n - 1] = nums[n - 1]
        prev_max = nums[n - 1]
        maximum = nums[n - 1]
        for i in range(n - 2, -1, -1):
            prev_max = max(nums[i], nums[i] + prev_max)
            maximum = max(maximum, prev_max)

            right[i] = maximum

        res = -sys.maxsize - 1
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])
        return res


# 方法二：前缀和
class Solution1:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0

        n = len(nums)
        # Maximum subarray value from left/right with n elements
        left = [0] * n
        right = [0] * n

        prefix_sum = 0
        min_sum = 0
        max_sum = -sys.maxsize - 1
        for i in range(n):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            left[i] = max_sum

        prefix_sum = 0
        min_sum = 0
        max_sum = -sys.maxsize - 1
        for i in range(n - 1, -1, -1):
            prefix_sum += nums[i]
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            right[i] = max_sum

        res = -sys.maxsize - 1
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])

        return res


if __name__ == '__main__':
    # 7
    print(Solution1().maxTwoSubArrays([1, 3, -1, 2, -1, 2]))
