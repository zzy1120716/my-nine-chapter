"""
943. Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j
(i ≤ j), inclusive.

样例
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
注意事项
You may assume that the array does not change.
There are many calls to sumRange function.
"""


# 注意是多次调用sumRange，所以使用前缀和
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0] * (len(nums) + 1)
        self.getPrefix(nums, self.prefix)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix[j + 1] - self.prefix[i]

    def getPrefix(self, nums, prefix):
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sumRange(0, 2))
    print(na.sumRange(2, 5))
    print(na.sumRange(0, 5))
