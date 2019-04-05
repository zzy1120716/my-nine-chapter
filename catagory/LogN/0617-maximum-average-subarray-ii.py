"""
617. 最大平均值子数组 II
给出一个整数数组，有正有负。找到这样一个子数组，他的长度大于等于 k，且平均值最大。

样例
给出 nums = [1, 12, -5, -6, 50, 3], k = 3

返回 15.667 // (-6 + 50 + 3) / 3 = 15.667

注意事项
保证数组的大小 >= k
"""


# 二分答案，注释版
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums:
            return 0
        # 二分答案起点，
        # 平均值必然小于等于数组最大值，
        # 大于等于数组最小值。
        start, end = min(nums), max(nums)
        # 最后的答案需满足的精度要求为1e-5
        while end - start > 1e-5:
            # 每次二分的目标平均值
            mid = (start + end) / 2
            # 寻找是否存在长度大于等于k的子数组，平均值大于mid
            if self.isExistGreaterAvg(nums, k, mid):
                # 存在，则目标平均值需增大
                start = mid
            else:
                # 否则，减小
                end = mid
        return start

    def isExistGreaterAvg(self, nums, k, avg):
        pre_sum = [0]
        for num in nums:
            # 此处存储的前缀和，是已经减去平均值的，
            # 后面判断只需与0比较即可。
            pre_sum.append(pre_sum[-1] + num - avg)

        min_pre_sum = 0
        for i in range(k, len(nums) + 1):
            # 存在比当前最小前缀和大的子数组，则返回True
            if pre_sum[i] - min_pre_sum >= 0:
                return True
            # 更新最小前缀和
            min_pre_sum = min(min_pre_sum, pre_sum[i - k + 1])
        return False


class Solution1:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums or k > len(nums):
            return 0
        start = min(nums)
        end = max(nums)

        eps = 1e-6
        # avg = 0

        while start + eps < end:
            avg = (start + end) / 2
            if self.check_avg(nums, k, avg):
                start = avg
            else:
                end = avg

        return start

    def check_avg(self, nums, k, avg):
        sub_sum = 0
        prev_sum = 0
        prev_min = 0

        for i in range(len(nums)):
            sub_sum += nums[i] - avg

            if i >= k - 1 and sub_sum >= 0:
                return True

            # 找一段长度 >= k 的子数组使它的平均值满足条件：
            # sub_sum 是 0 到 i 所有元素之和，而 prev_sum 是 0 到 i - k 的所有元素之和，
            # 这样可以保证用 sub_sum - prev_sum 的数组长度比 k 长，
            # prev_min 来记录 prev_sum 的最小值，通过 sub_sum 减去 prev_sum 来获得子数组可能的最大值。
            if i >= k:
                prev_sum += nums[i - k] - avg
                prev_min = min(prev_min, prev_sum)
                if sub_sum - prev_min >= 0:
                    return True

        return False


# 二分答案，二分出 average 之后，把数组中的每个数都减去 average，
# 然后的任务就是去求这个数组中，是否有长度 >= k 的 subarray，它的和超过 0。
# 这一步用类似 Maximum Subarray 的解法来做就好了
class Solution2:
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