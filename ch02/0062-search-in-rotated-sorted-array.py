"""
62. 搜索旋转排序数组
假设有一个排序的按未知的旋转轴旋转的数组
(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。
给定一个目标值进行搜索，如果在数组中找到目标值
返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

样例
给出[4, 5, 1, 2, 3]和target=1，返回 2

给出[4, 5, 1, 2, 3]和target=0，返回 -1

挑战
O(logN) time
"""


# 方法一：一次二分
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if A[mid] == target:
                return mid
            
            if A[start] < A[mid]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
        
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


# 方法二：先找到最小值，再二分搜索有序的区间
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        min_idx = self.findMin(nums)
        if nums[min_idx] <= target <= nums[-1]:
            return self.binarySearch(nums, min_idx, len(nums) - 1, target)
        return self.binarySearch(nums, 0, min_idx - 1, target)

    def findMin(self, nums):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return start
        return end

    def binarySearch(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    print(Solution1().search([4, 5, 1, 2, 3], 1))
    print(Solution1().search([4, 5, 1, 2, 3], 0))
