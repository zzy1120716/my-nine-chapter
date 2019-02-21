"""
374. 螺旋矩阵
中文English
给定一个包含 m x n 个要素的矩阵，（m 行, n 列），按照螺旋顺序，返回该矩阵中的所有要素。

样例
给定如下矩阵：

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
应返回 [1,2,3,6,9,8,7,4,5]。
"""


class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        res = []

        if len(matrix) == 0:
            return res

        rows = len(matrix)
        columns = len(matrix[0])

        start = 0
        # 继续打印的条件是columns > start * 2，并且rows > start * 2
        while columns > start * 2 and rows > start * 2:
            res.extend(self.printMatrixInCircle(matrix, rows, columns, start))
            start += 1

        return res

    # 打印一圈
    def printMatrixInCircle(self, matrix, rows, columns, start):
        circleRes = []
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX + 1):
            circleRes.append(matrix[start][i])

        # 从上到下打印一列
        if start < endY:
            for i in range(start + 1, endY + 1):
                circleRes.append(matrix[i][endX])

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX - 1, start - 1, -1):
                circleRes.append(matrix[endY][i])

        # 从下到上打印一列
        if start < endX and start < endY - 1:
            for i in range(endY - 1, start, -1):
                circleRes.append(matrix[i][start])

        return circleRes


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

