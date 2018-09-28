"""
585. 山脉序列中的最大值
给 n 个整数的山脉数组，即先增后减的序列，找到山顶（最大值）

样例
给出数组为 [1, 2, 4, 8, 6, 3],返回 8
给出数组为 [10, 9, 8, 7]，返回 10
"""
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 0
            
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
                
        return max(nums[start], nums[end])