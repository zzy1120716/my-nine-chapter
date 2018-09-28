"""
464. 整数排序 II
给一组整数，按照升序排序。使用归并排序，快速排序，
堆排序或者任何其他 O(n log n) 的排序算法。

样例
给出 [3, 2, 1, 4, 5], 排序后的结果为 [1, 2, 3, 4, 5]。
"""

# 快排
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return
        
        self.quickSort(A, 0, len(A) - 1)
        
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[(start + end) // 2]
        
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
            
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

# 归并
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return
        
        temp = [0 for _ in range(len(A))]
        
        self.merge_sort(A, 0, len(A) - 1, temp)
        
    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid + 1, end, temp)
        self.merge(A, start, mid, end, temp)
        
    def merge(self, A, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start
        
        while left <= mid and right <= end:
            if A[left] < A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1
            index += 1
            
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
            
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
            
        for i in range(start, end + 1):
            A[i] = temp[i]