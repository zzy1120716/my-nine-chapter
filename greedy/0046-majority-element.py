"""
46. Majority Element
给定一个整型数组，找出主元素，它在数组中的出现次数严格大于
数组元素个数的二分之一。

样例
给出数组[1,1,1,1,2,2,2]，返回 1

挑战
要求时间复杂度为O(n)，空间复杂度为O(1)

注意事项
You may assume that the array is non-empty and the majority 
number always exist in the array.
"""
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        key, count = None, 0
        for num in nums:
            if key is None:
                key, count = num, 1
            else:
                if key == num:
                    count += 1
                else:
                    count -= 1
            
            if count == 0:
                key = None
        
        return key