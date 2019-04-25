"""
1291. 矩阵中的最长递增路径

给定整数矩阵，找到最长递增路径的长度。

从每个单元格，您可以移动到四个方向：左，右，上或下。 您可能不会沿对角线移动或移动到边界之外（即不允许环绕）。

样例
样例 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
返回 4
最长递增路径是 [1, 2, 6, 9]。

样例 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
返回 4
最长递增路径是 [3, 4, 5, 6]。 不可以沿对角线移动。
"""


# DFS + 记忆化
class Solution:

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self):
        self.ans = 0

    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    def longestIncreasingPath(self, matrix):
        # write your code here
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        memo = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.ans = max(self.ans, self.dfs(matrix, i, j, m, n, memo))
        return self.ans

    def dfs(self, matrix, x, y, m, n, memo):
        if memo[x][y] != -1:
            return memo[x][y]
        memo[x][y] = 1
        for dx, dy in self.DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] <= matrix[x][y]:
                continue
            memo[x][y] = max(memo[x][y], 1 + self.dfs(matrix, nx, ny, m, n, memo))
        return memo[x][y]


# DP
class Solution1:

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    def longestIncreasingPath(self, matrix):
        # write your code here
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        ans = 0
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((matrix[i][j], (i, j)))
        cells.sort(reverse=True)
        for cell in cells:
            x = cell[1][0]
            y = cell[1][1]
            for dx, dy in self.DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if matrix[nx][ny] <= matrix[x][y]:
                    continue
                dp[x][y] = max(dp[x][y], 1 + dp[nx][ny])
            ans = max(ans, dp[x][y])
        return ans


if __name__ == '__main__':
    print(Solution1().longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]))     # 4
