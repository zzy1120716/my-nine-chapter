"""
461. 无序数组K小元素
找到一个无序数组中第K小的数

样例
[3, 4, 1, 2, 5], k = 3, 第三小的数是3

挑战
O(nlogn)的非常简单，是否可以O(n)
"""
class Solution:

    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        # python starts from 0 -> k-1
        return self.quick_select(0, len(nums) - 1, nums, k - 1)

    def quick_select(self, start, end, nums, k):
        # during the process, it's guaranteed start <= k <= end
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # left is not bigger than right
        # 在左边区间找
        if right >= k:
            self.quick_select(start, right, nums, k)
        # 在右边区间找
        if left <= k:
            self.quick_select(left, end, nums, k)

        return nums[k]