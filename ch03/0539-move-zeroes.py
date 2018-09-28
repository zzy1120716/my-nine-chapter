"""
539. 移动零
给一个数组 nums 写一个函数将 0 移动到数组的最后面，
非零元素保持原数组的顺序

样例
给出 nums = [0, 1, 0, 3, 12], 调用函数之后,
nums = [1, 3, 12, 0, 0].

注意事项
1.必须在原数组上操作
2.最小化操作数
"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1