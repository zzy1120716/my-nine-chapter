"""
373. 奇偶分割数组
中文English
分割一个整数数组，使得奇数在前偶数在后。

样例
给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。

挑战
在原数组中完成，不使用额外空间。
"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        odd, even = 0, len(nums) - 1
        while odd < even:
            while odd < even and nums[odd] & 1 == 1:
                odd += 1
            while odd < even and nums[even] & 1 == 0:
                even -= 1
            if odd < even:
                nums[odd], nums[even] = nums[even], nums[odd]
                odd += 1
                even -= 1
