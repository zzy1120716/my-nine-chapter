"""
28. 搜索二维矩阵
写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
样例
考虑下列矩阵：

[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

挑战
O(log(n) + log(m)) 时间复杂度
"""

"""
方法一：两次二分，先确定行，再确定行中是否有target
"""
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or len(matrix) == 0:
            return False

        row, col = len(matrix), len(matrix[0])
        start, end = 0, row - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False

        start, end = 0, col - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid
            else:
                end = mid

        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        else:
            return False


"""
方法二：一次二分
"""
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False

        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1

        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid // col, mid % col
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid

        x, y = start // col, start % col
        if matrix[x][y] == target:
            return True

        x, y = end // col, end % col
        if matrix[x][y] == target:
            return True

        return False
