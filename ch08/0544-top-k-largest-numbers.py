"""
544. 前K大数
在一个数组中找到前K大的数

样例
给出 [3,10,1000,-99,4,100], k = 3.
返回 [1000, 100, 10]
"""


# 方法一：quick select
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        self.quickSelect(nums, 0, len(nums) - 1, k)
        res = nums[:k]
        res.sort(reverse=True)
        return res

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return

        pivot = nums[start]
        i, j = start, end
        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1

            while i <= j and nums[j] < pivot:
                j -= 1

            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if start + k - 1 <= j:
            self.quickSelect(nums, start, j, k)

        if start + k - 1 >= i:
            self.quickSelect(nums, i, end, k - (i - start))


# 方法二：quick select partition函数
class Solution1:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        start = 0
        end = len(nums) - 1
        index = self.partition(nums, start, end)
        while index != len(nums) - k:
            if index > len(nums) - k:
                end = index - 1
                index = self.partition(nums, start, end)
            else:
                start = index + 1
                index = self.partition(nums, start, end)
        result = nums[index:]
        result.sort()
        return result[::-1]

    def partition(self, A, start, end):
        index = start
        for i in range(start, end):
            if A[i] > A[end]:
                continue
            A[index], A[i] = A[i], A[index]
            index += 1
        A[index], A[end] = A[end], A[index]
        return index


# 方法三：trick
import heapq


class Solution2:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        return heapq.nlargest(k, nums)