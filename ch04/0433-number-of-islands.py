"""
433. 岛屿的个数
给一个01矩阵，求不同的岛屿的个数。

0代表海，1代表岛，如果两个1相邻，那么这两个1属于
同一个岛。我们只考虑上下左右为相邻。

样例
在矩阵：

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
中有 3 个岛.
"""


# 方法一：BFS
from queue import Queue


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        islands = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    self.markByBFS(grid, i, j)
                    islands += 1
        
        return islands
        
    def markByBFS(self, grid, x, y):
        directionX = [0, 1, -1, 0]
        directionY = [1, 0, 0, -1]
        
        q = Queue()
        q.put(Coordinate(x, y))
        grid[x][y] = False
        
        while not q.empty():
            coor = q.get()
            for i in range(4):
                adj = Coordinate(coor.x + directionX[i], coor.y + directionY[i])
                if not self.inBound(adj, grid):
                    continue
                if grid[adj.x][adj.y]:
                    grid[adj.x][adj.y] = False
                    q.put(adj)
    
    def inBound(self, coor, grid):
        n = len(grid)
        m = len(grid[0])
        return n > coor.x >= 0 and m > coor.y >= 0


# 方法二：DFS
class Solution1:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
            
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                ans += 1
                self.dfs(grid, i, j)
        return ans
        
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        
        if grid[i][j]:
            grid[i][j] = False
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)


if __name__ == '__main__':
    print(Solution().numIslands([
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1]
    ]))
