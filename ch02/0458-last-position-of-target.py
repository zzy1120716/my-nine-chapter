"""
458. 目标最后位置
给一个升序数组，找到target最后一次出现的位置，
如果没出现过返回-1

样例
给出 [1, 2, 2, 4, 5, 5].

target = 2, 返回 2.

target = 5, 返回 5.

target = 6, 返回 -1.
"""
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if nums is None or len(nums) == 0:
            return -1
            
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                start = mid
            
            elif nums[mid] < target:
                start = mid
            
            else:
                end = mid
        
        if nums[end] == target:
            return end
            
        if nums[start] == target:
            return start
        
        return -1