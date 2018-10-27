"""
573. 邮局的建立 II
给出一个二维的网格，每一格可以代表墙 2 ，房子 1，以及空 0 (用数字0,1,2来表示)，
在网格中找到一个位置去建立邮局，使得所有的房子到邮局的距离和是最小的。

返回所有房子到邮局的最小距离和，如果没有地方建立邮局，则返回-1.

样例
给出一个网格：

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
返回 8，你可以在(1,1)处建立邮局 (在(1,1)处建立邮局，所有房子到邮局的距离是最近的)。

挑战
在O(n^3)内的时间复杂度解决此问题。

注意事项
你不能穿过房子和墙，只能穿过空地。
你只能在空地建立邮局。
"""

"""
对每个 house 做 BFS，

记录每个 empty：
1. 能被多少个 house 触及
2. 这些能触及的 house 到达这个 empty 的总步数之和

如果最后每个 empty 都无法被所有 house 触及 (即不等于 house 个数)，则返回 -1
如果有能被所有 house 触及的 empty，取其最小的返回
"""


class Solution:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

    INFINITY = float('inf')
    MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))

    visited_time = None
    distance_sum = None

    """
    @param grid: a 2D grid
    @return: An integer
    """

    def shortestDistance(self, grid):
        # write your code here
        if not grid:
            return -1

        self.row, self.col = len(grid), len(grid[0])
        self.visited_time = [[0] * self.col for _ in range(self.row)]
        self.distance_sum = [[0] * self.col for _ in range(self.row)]

        house_count = 0
        for x in range(self.row):
            for y in range(self.col):
                if grid[x][y] == self.HOUSE:
                    house_count += 1
                    self.bfs(x, y, grid)

        min_distance = self.INFINITY
        for x in range(self.row):
            for y in range(self.col):
                if grid[x][y] == self.EMPTY \
                        and self.visited_time[x][y] == house_count \
                        and self.distance_sum[x][y] < min_distance:
                    min_distance = self.distance_sum[x][y]

        return min_distance if min_distance < self.INFINITY else -1

    def bfs(self, x, y, grid):
        queue, new_queue = [(x, y)], None
        visited = [[False] * self.col for _ in range(self.row)]
        distance = 0

        while queue:
            new_queue = []
            distance += 1
            for x, y in queue:
                for dx, dy in self.MOVES:
                    nx = x + dx
                    ny = y + dy
                    if nx >= 0 and nx < self.row and ny >= 0 and ny < self.col \
                            and grid[nx][ny] == self.EMPTY \
                            and not visited[nx][ny]:
                        visited[nx][ny] = True
                        self.visited_time[nx][ny] += 1
                        self.distance_sum[nx][ny] += distance
                        new_queue.append((nx, ny))
            queue = new_queue