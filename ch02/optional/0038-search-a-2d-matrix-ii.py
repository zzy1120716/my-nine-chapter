"""
38. 搜索二维矩阵 II
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
样例
考虑下列矩阵：

[

    [1, 3, 5, 7],

    [2, 4, 7, 8],

    [3, 5, 9, 10]

]

给出target = 3，返回 2

挑战
要求O(m+n) 时间复杂度和O(1) 额外空间
"""

"""
方法一：暴力法 O(m * n)
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        res = 0
        for row in matrix:
            if row[0] > target:
                break
            for num in row:
                if num > target:
                    break
                if num == target:
                    res += 1
        return res


"""
方法二：O(m + n)
"""
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        row, col = len(matrix), len(matrix[0])
        # 从矩阵的左下角开始找
        i, j = row - 1, 0
        count = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count