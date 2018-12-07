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


# Misra-Gries Family of Algorithms - MAJORITY problem
# https://zhenye-na.github.io/2018/05/13/misra-gries-algorithms.html#majority-problem

"""
O(n) time and O(1) extra space

Let us look at the MAJORITY problem first. We have two variables that we store. 
The first-variable is the key (which is either a member of 1,2,…,m or a null-entity). 
The second-variable is an integer (which is a count). We start with an empty key, and a count of zero.

Every time an element a_i = j of the data-stream is observed,

If the key is empty we set the value of the key to j, and we initialize the count to 1.
If the key is not empty, and equal to j, we increment the count by 1.
If the key is not empty, and not equal to j, we decrement the count by 1
If the count becomes zero as a result of this decrementing, we set the key to null-entity.

It is not hard to see that if there is a majority-element, it will be the value of the key.
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