"""
459. 排序数组中最接近元素
在一个排好序的数组 A 中找到 i 使得 A[i] 最接近 target

样例
[1, 2, 3] target = 2, 返回 1.
[1, 4, 6] target = 3, 返回 1.
[1, 4, 6] target = 5, 返回 1 或者 2.
[1, 3, 3, 4] target = 2, 返回 0 或者 1 或者 2.

挑战
O(logn) time complexity.

注意事项
There can be duplicate elements in the array, and we can return any of the indices with same value.
"""
class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        return start if target - A[start] < A[end] - target else end