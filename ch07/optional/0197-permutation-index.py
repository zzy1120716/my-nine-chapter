"""
197. 排列序号
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。
其中，编号从1开始。

样例
例如，排列 [1,2,4] 是第 1 个排列。
"""


# 正序利用权值计算index
class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        # 至少为1，初始的全排列为增序，index记录第几个全排列
        index = 1
        for i in range(len(A)):
            # count记录该数后面有几个比它小的数字
            count = 0
            # factor用来计算阶乘的权值
            factor = 1
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    count += 1
            if count > 0:
                for k in range(1, len(A) - i):
                    factor *= k
            index = (factor * count) + index
        return index
