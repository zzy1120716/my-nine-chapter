"""
65. 两个排序数组的中位数
两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，
要求时间复杂度应为O(log (m+n))。

样例
给出数组A = [1,2,3,4,5,6] B = [2,3,4,5]，中位数3.5

给出数组A = [1,2,3] B = [4,5]，中位数 3

挑战
时间复杂度为O(log n)
"""


# 方法一：sort O(nlogn)
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        C = sorted(A + B)
        n = len(C)
        return C[n // 2] if n % 2 != 0 else (C[n // 2] + C[n // 2 - 1]) / 2


# 方法二：merge只计数，不开辟新空间 O(n)
class Solution1:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        i = j = m1 = m2 = 0

        while i + j <= n / 2:
            if i < len(A) and j < len(B):
                m2 = m1
                if A[i] < B[j]:
                    m1 = A[i]
                    i += 1
                else:
                    m1 = B[j]
                    j += 1
            elif i < len(A):
                m2 = m1
                m1 = A[i]
                i += 1
            elif j < len(B):
                m2 = m1
                m1 = B[j]
                j += 1

        if n % 2 == 0:
            return (m1 + m2) / 2.0
        else:
            return m1


# 方法三：二分答案 O(logn)
class Solution2:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0
