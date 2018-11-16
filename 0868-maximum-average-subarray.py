"""
868. Maximum Average Subarray
给定一个由n个整数组成的数组，找到给定长度k的连续子数组，该子数组具有最大平均值。
你需要输出最大平均值。

样例
给定nums = [1,12,-5,-6,50,3]， k = 4，返回12.75

解释：
最大平均为(12-5-6+50)/4 = 51/4 = 12.75。
注意事项
1 <= k <= n <= 30,000.
给定数组的元素将在范围[-10,000, 10,000]。
"""


class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        subsum = 0
        for i in range(k):
            subsum += nums[i]
        maxsum = subsum
        for i in range(k, len(nums)):
            subsum = subsum - nums[i - k] + nums[i]
            maxsum = max(maxsum, subsum)
        return maxsum / k


if __name__ == '__main__':
    print(Solution().findMaxAverage([7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7))
