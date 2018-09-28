"""
159. 寻找旋转排序数组中的最小值
假设一个旋转排序的数组其起始位置是未知的
（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

你可以假设数组中不存在重复的元素。

样例
给出[4,5,6,7,0,1,2]  返回 0

注意事项
You may assume no duplicate exists in the array.
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
            
        start, end, target = 0, len(nums) - 1, nums[len(nums) - 1]
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] > target:
                start = mid
            else:
                end = mid
        
        if nums[start] < target:
            return nums[start]
        else:
            return nums[end]