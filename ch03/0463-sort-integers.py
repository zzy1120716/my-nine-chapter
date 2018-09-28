"""
463. 整数排序
给一组整数，按照升序排序，使用选择排序，冒泡排序，
插入排序或者任何 O(n2) 的排序算法。

样例
对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]。
"""
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        if A is None or len(A) == 0:
            return
        
        # write your code here
        for i in range(len(A)):
            for j in range(1, len(A) - i):
                if A[j - 1] > A[j]:
                    A[j - 1], A[j] = A[j], A[j - 1]