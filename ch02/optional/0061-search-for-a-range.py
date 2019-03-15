"""
61. 搜索区间
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]

样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]

挑战
时间复杂度 O(log n)
"""


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A or target is None:
            return [-1, -1]

        return [self.bisectLeft(A, target), self.bisectRight(A, target)]

    def bisectLeft(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1

    def bisectRight(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        return -1


class Solution1:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
                while low < high and nums[high - 1] == nums[high]:
                    high -= 1
            elif nums[mid] < target:
                low = mid + 1
                while low < high and nums[low + 1] == nums[low]:
                    low += 1
            else:
                low = high = mid
                while low > 0 and nums[low - 1] == nums[low]:
                    low -= 1
                while high < len(nums) - 1 and nums[high + 1] == nums[high]:
                    high += 1
                return [low, high]
        return [-1, -1]
