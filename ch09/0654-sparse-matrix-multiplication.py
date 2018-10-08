"""
654. 稀疏矩阵乘法
给定两个 稀疏矩阵 A 和 B，返回AB的结果。
您可以假设A的列数等于B的行数。

样例
A = [
   [ 1, 0, 0],
   [-1, 0, 3]
]

B = [
   [ 7, 0, 0 ],
   [ 0, 0, 0 ],
   [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

"""
方法一：普通方法
"""
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        m, n, s = len(A), len(B), len(B[0])
        C = [[0] * s for _ in range(m)]
        for i in range(m):
            for j in range(s):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C


"""
方法二：先找到所有非零的点
"""
class Element:  # point in matrix
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply(self, A, B):
        # write your code here
        elements_A = self._get_non_zero_elements(A)
        elements_B = self._get_non_zero_elements(B)

        C = [[0] * len(B[0]) for _ in range(len(A))]

        for elem_A in elements_A:
            for elem_B in elements_B:
                if elem_A.col == elem_B.row:
                    C[elem_A.row][elem_B.col] += elem_A.val * elem_B.val

        return C

    def _get_non_zero_elements(self, A):
        elements = []

        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 0:
                    continue

                elements.append(Element(A[row][col], row, col))

        return elements
