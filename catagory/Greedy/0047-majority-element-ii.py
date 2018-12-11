"""
47. Majority Element II
给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的三分之一。


样例
给出数组[1,2,1,2,1,3,3] 返回 1

挑战
要求时间复杂度为O(n)，空间复杂度为O(1)。

注意事项
数组中只有唯一的主元素
"""


# Boyer-Moore Majority Vote algorithm
class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        if nums.count(candidate1) > len(nums) // 3:
            return candidate1
        elif nums.count(candidate2) > len(nums) // 3:
            return candidate2
        return
