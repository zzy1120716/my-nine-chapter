"""
598. 僵尸矩阵
给一个二维网格，每一个格子都有一个值，2 代表墙，1 代表僵尸，0 代表人类(数字 0, 1, 2)。
僵尸每天可以将上下左右最接近的人类感染成僵尸，但不能穿墙。将所有人类感染为僵尸需要多久，
如果不能感染所有人则返回 -1。

样例
给一个矩阵：

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
返回 2
"""


# 方法一：问题与墙的坐标其实无关，只要遇到1边上的0，立即变成1就行了
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        row, col = len(grid), len(grid[0])
        if not row or not col:
            return 0

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        days = 0

        # push all zombies' coordinates into a queue
        q = self.get_zombies(grid)

        while q:
            days += 1
            new_q = []
            # zombie location (x, y)
            for x, y in q:
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    # position can be infected
                    if row > nx >= 0 and col > ny >= 0 and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        new_q.append((nx, ny))
            # renew zombie queue with recent infected people
            q = new_q

        # check if there any person left
        if not self.is_all_infected(grid):
            return -1
        return days - 1

    """
    @param grid: a 2D integer grid
    @return: a list
    """
    def get_zombies(self, grid):
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
        return queue

    """
    @param grid: a 2D integer grid
    @return: a boolean
    """
    def is_all_infected(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return False
        return True


# 方法二：记录墙和僵尸的数量，队列中每一项增加当前僵尸数量，
# 省去存储天数的变量，以及简化判断是否都被感染的步骤
class Solution1:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        sum_zombie = 0
        sum_wall = 0
        row = len(grid)
        col = len(grid[0])
        qzombie = []
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    qzombie.append([i, j, 0])
                    sum_zombie += 1
                elif grid[i][j] == 2:
                    sum_wall += 1

        step = 0
        while qzombie:
            p = qzombie.pop(0)
            for i in range(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if x < 0 or x >= row or y < 0 or y >= col:
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    qzombie.append([x, y, p[2] + 1])
                    sum_zombie += 1
            if not qzombie:
                step = p[2]

        if sum_zombie + sum_wall != row * col:
            return -1
        else:
            return step


if __name__ == '__main__':
    print(Solution().zombie([
        [0, 1, 2, 0, 0],
        [1, 0, 0, 2, 1],
        [0, 1, 0, 0, 0]
    ]))
