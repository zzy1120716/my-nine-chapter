"""
462. 目标出现总和
给一个升序的数组，以及一个target，找到它在数组中出现的次数。

样例
给出 [1, 3, 3, 4, 5] target = 3, 返回 2.

给出 [2, 2, 3, 4, 6] target = 4, 返回 1.

给出 [1, 2, 3, 4, 5] target = 6, 返回 0.

挑战
Time complexity in O(logn)
"""

"""
使用两次二分，分别找到元素第一次和最后一次出现的位置。
"""
class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A or target is None:
            return 0
        left = self.binarySearchLeft(A, target)
        right = self.binarySearchRight(A, target)
        if left == -1 or right == -1:
            return 0
        else:
            return right - left + 1


    def binarySearchLeft(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1


    def binarySearchRight(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            return end
        elif A[start] == target:
            return start
        else:
            return -1