"""
665. 平面范围求和 -不可变矩阵
给一 二维矩阵,计算由左上角 (row1, col1) 和右下角 (row2, col2) 划定的矩形内元素和.

样例
给出矩阵

[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

注意事项
你可以假设矩阵不变
对函数 sumRegion 的调用次数有很多次
你可以假设 row1 ≤ row2 并且 col1 ≤ col2
"""


# 方法一：Caching Rows
# 还记得我们使用累积和数组的1D版本吗？我们可以直接应用它来解决这个2D版本
# 尝试将2D矩阵视为m行的1D阵列。为了找到区域总和，我们只是逐行累积区域中的总和。
class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(m):
                self.dp[r][c + 1] = self.dp[r][c] + matrix[r][c]

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        ans = 0
        for i in range(row1, row2 + 1):
            ans += self.dp[i][col2 + 1] - self.dp[i][col1]
        return ans


# 方法二：Caching Smarter
# 我们在1D版本中使用了累积和数组。 我们注意到累积和是相对于索引0处的原点计算的。
# 将这个类比扩展到2D情况，我们可以预先计算相对于原点的累积区域和(0,0)。
# sum(ABCD) = sum(OD) - sum(OB) - sum(OC) + sum(OA)
class NumMatrix1:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        n = len(matrix)
        m = len(matrix[0])
        self.dp = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(m):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


if __name__ == '__main__':
    nm = NumMatrix1([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])
    print(nm.sumRegion(2, 1, 4, 3))
    print(nm.sumRegion(1, 1, 2, 2))
    print(nm.sumRegion(1, 2, 2, 4))
