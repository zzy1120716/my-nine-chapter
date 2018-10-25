"""
443. 两数之和 II
给一组整数，问能找出多少对整数，他们的和大于一个给定的目标值。

样例
对于 numbers = [2, 7, 11, 15], target = 24 的情况，返回 1。因为只有11 + 15可以大于24。

挑战
Do it in O(1) extra space and O(nlogn) time.
"""

"""
双指针，类似两数之和小于等于目标值那道题
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                count += right - left
                right -= 1
            else:
                left += 1
        return count
