"""
617. 最大平均值子数组 II
给出一个整数数组，有正有负。找到这样一个子数组，他的长度大于等于 k，且平均值最大。

样例
给出 nums = [1, 12, -5, -6, 50, 3], k = 3

返回 15.667 // (-6 + 50 + 3) / 3 = 15.667

注意事项
保证数组的大小 >= k
"""


# 二分答案，二分出 average 之后，把数组中的每个数都减去 average，
# 然后的任务就是去求这个数组中，是否有长度 >= k 的 subarray，它的和超过 0。
# 这一步用类似 Maximum Subarray 的解法来做就好了
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def check_subarray(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
        return False


if __name__ == '__main__':
    print(Solution().maxAverage([1, 12, -5, -6, 50, 3], 3))