"""
64. 合并排序数组
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出 A = [1, 2, 3, empty, empty], B = [4, 5]

合并之后 A 将变成 [1,2,3,4,5]

注意事项
你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
"""

"""
方法一：B中所有数加到A末尾，再排序O(nlogn))
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(n):
            A[i + m] = B[i]
        A.sort()

"""
方法二：双指针，从末尾开始遍历，取较大值加到A的末尾，O(n)
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j, index = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[index] = B[j]
                j -= 1
            else:
                A[index] = A[i]
                i -= 1
            index -= 1

        while j >= 0:
            A[index] = B[j]
            index -= 1
            j -= 1