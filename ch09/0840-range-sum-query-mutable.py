"""
840. 可变范围求和
Given an integer array nums, find the sum of the elements between
indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element
at index i to val.

样例
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
注意事项
1.The array is only modifiable by the update function.
2.You may assume the number of calls to update and sumRange function
s distributed evenly.
"""

"""
树状数组（Binary Index Tree）
https://blog.csdn.net/Yaokai_AssultMaster/article/details/79492190
"""

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0 for i in range(len(nums))]
        self.bitree = [0 for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[i]
        self.arr[i] = val
        index = i + 1

        while index <= len(self.arr):
            self.bitree[index - 1] += delta
            index += self.lowbit(index)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getPrefixSum(j) - self.getPrefixSum(i - 1)

    def getPrefixSum(self, i):
        sum = 0
        index = i + 1
        while index > 0:
            sum += self.bitree[index - 1]
            index -= self.lowbit(index)

        return sum

    def lowbit(self, x):
        return x & -x

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)