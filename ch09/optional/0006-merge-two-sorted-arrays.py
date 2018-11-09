"""
6. 合并排序数组 II
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战
你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
"""


# 方法一：普通归并
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        i = j = 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
        return C


# 方法二：二分查找并插入
class Solution1:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        # make B the smaller one
        if len(A) < len(B):
            A, B = B, A

        # binary search and insert
        for num in B:
            left = 0
            right = len(A) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if num < A[mid]:
                    right = mid
                else:
                    left = mid

            if num < A[left]:
                A.insert(left, num)
            elif num > A[right]:
                A.insert(right + 1, num)
            else:
                A.insert(right, num)

        return A


if __name__ == '__main__':
    A = Solution1().mergeSortedArray([1, 2, 3, 4], [2, 4, 5, 6])
    print(A)
