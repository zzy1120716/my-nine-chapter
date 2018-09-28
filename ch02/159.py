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