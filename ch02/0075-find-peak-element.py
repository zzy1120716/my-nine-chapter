"""
75. 寻找峰值
你给出一个整数数组(size为n)，其具有以下特点：

相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，
返回数组中任意一个峰值的位置。

样例
给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2
所在位置, 或者6, 即数值 7 所在位置.

挑战
Time complexity O(logN)

注意事项
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
"""
class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return -1
            
        start, end = 1, len(A) - 2
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        
        return start if A[start] > A[end] else end