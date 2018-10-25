"""
609. 两数和-小于或等于目标值
给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。

样例
给定数组为 [2,7,11,15]，目标值为 24
返回 5。
2+7<24
2+11<24
2+15<24
7+11<24
7+15<24
"""

"""
方法一：双指针，一头一尾
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                # 最右边的数加上左边的数小于等于target
                # 必有它们之间所有数都小于等于target
                count += right - left
                left += 1
            else:
                right -= 1
        return count


"""
方法二：使用二分查找右边满足条件
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        count = 0

        for i in range(len(nums) - 1):
            start, end, val = i + 1, len(nums) - 1, target - nums[i]
            while start + 1 < end:
                mid = (start + end) // 2
                if nums[mid] <= val:
                    start = mid
                else:
                    end = mid

            if nums[end] <= val:
                count += end - i
            elif nums[start] <= val:
                count += start - i

        return count