"""
457. 经典二分查找问题
在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1

样例
给出数组 [1, 2, 2, 4, 5, 5].

对于 target = 2, 返回 1 或者 2.
对于 target = 5, 返回 4 或者 5.
对于 target = 6, 返回 -1.
挑战
O(logn) 的时间
"""


import bisect


class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1


class Solution1:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        if not nums or target is None:
            return -1

        start, end = 0, len(nums) - 1

        if target < nums[start] or target > nums[end]:
            return -1

        while start + 1 < end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid

        if target == nums[end]:
            return end
        elif target == nums[start]:
            return start
        else:
            return -1


if __name__ == '__main__':
    print(Solution().findPosition([1, 2, 2, 4, 5, 5], 2))
    print(Solution().findPosition([1, 2, 2, 4, 5, 5], 5))
    print(Solution().findPosition([1, 2, 2, 4, 5, 5], 6))
