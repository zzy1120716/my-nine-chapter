"""
931. Median of K Sorted Arrays
There are k sorted arrays nums. Find the median of the given k sorted arrays.

样例
Given nums = [[1],[2],[3]], return 2.00.

注意事项
The length of the given arrays may not equal to each other.
The elements of the given arrays are all positive number.
Return 0 if there are no elements in the array.
"""

"""
方法一：合并 + 排序
"""
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        A = []
        for arr in nums:
            A.extend(arr)
        if not A:
            return float(0)
        A.sort()
        l = len(A)
        return float((A[l // 2] + A[l // 2 - 1]) / 2) if l % 2 == 0 else float(A[l // 2])

"""
方法二：归并排序，会超时
"""
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        A = []
        for n in nums:
            A = self.mergeSorted(A, n)
        if not A:
            return float(0)
        l = len(A)
        return float([A[l//2],(A[l//2] + A[l//2-1])/2][l%2==0])

    def mergeSorted(self, a, b):
        i, j, res = len(a) - 1, len(b) - 1, []
        while i >= 0 or j >= 0:
            if i < 0 or (i >= 0 and j >= 0 and a[i] < b[j]):
                res = [b[j]] + res
                j -= 1
            else:
                res = [a[i]] + res
                i -= 1
        return res

"""
方法三：二分答案
"""
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """

    def findMedian(self, nums):
        # write your code here
        if not nums:
            return 0.0

        size = self.get_total_size(nums)
        if size == 0:
            return 0.0

        smallest, largest = math.inf, - math.inf
        for arr in nums:
            if not arr:
                continue
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])

        # odd size => get the median directly
        if size % 2 == 1:
            return float(self.get_kth_number(nums, size // 2 + 1, smallest, largest))

        left = self.get_kth_number(nums, size // 2, smallest, largest)
        right = self.get_kth_number(nums, size // 2 + 1, left, largest)
        return (left + right) / 2

    # k is not zero-based, it starts from 1.
    def get_kth_number(self, nums, k, start, end):
        # find the last number x that >= k numbers are >= x.
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.number_of_numbers_less_than_or_equal_to(nums, mid) >= k:
                end = mid
            else:
                start = mid

        if self.number_of_numbers_less_than_or_equal_to(nums, start) >= k:
            return start

        return end

    # get how many numbers greater than or equal to val in 2d array
    def number_of_numbers_less_than_or_equal_to(self, nums, number):
        number_of_smaller_or_equal = 0
        for arr in nums:
            if not arr:
                continue
            if arr[0] > number:
                continue
            number_of_smaller_or_equal += self.get_number_of_smaller_or_equal(arr, number)
        return number_of_smaller_or_equal

    # get how many numbers greater than or equal to val in an array
    def get_number_of_smaller_or_equal(self, arr, number):
        start, end = 0, len(arr) - 1

        # find first element >= val
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] <= number:
                start = mid
            else:
                end = mid

        if arr[end] <= number:
            return end + 1
        if arr[start] <= number:
            return start + 1
        return 0

    def get_total_size(self, nums):
        size = 0
        for arr in nums:
            size += len(arr)
        return size