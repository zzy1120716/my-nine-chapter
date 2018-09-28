"""
62. 搜索旋转排序数组
假设有一个排序的按未知的旋转轴旋转的数组
(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。
给定一个目标值进行搜索，如果在数组中找到目标值
返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

样例
给出[4, 5, 1, 2, 3]和target=1，返回 2

给出[4, 5, 1, 2, 3]和target=0，返回 -1

挑战
O(logN) time
"""
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if A[mid] == target:
                return mid
            
            if A[start] < A[mid]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1