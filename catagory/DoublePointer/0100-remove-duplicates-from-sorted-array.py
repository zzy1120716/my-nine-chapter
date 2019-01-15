"""
100. 删除排序数组中的重复数字
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        temp = nums[0]
        j = 1
        while j < len(nums):
            if nums[j] == temp:
                nums.pop(j)
            else:
                temp = nums[j]
                j += 1
        return j + 1


# 从后向前遍历
class Solution1:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        tmp = None
        for i in range(len(nums), 0, -1):
            if tmp == nums[i - 1]:
                nums.pop(i - 1)
            else:
                tmp = nums[i - 1]
        return len(nums)
