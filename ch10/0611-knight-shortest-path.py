"""
611. 骑士的最短路线
给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空 1 表示有障碍物)，
找到到达 终点 的最短路线，返回路线的长度。如果骑士不能到达则返回 -1 。

样例
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
说明
如果骑士的位置为 (x,y)，他下一步可以到达以下这些位置:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
注意事项
起点跟终点必定为空.
骑士不能穿过障碍物.
"""

"""
方法一：BFS层级遍历
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Solution:

    move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param coord: a point
    @return: is valid bool True or False
    """
    def checkValid(self, grid, coord):
        row = len(grid)
        col = len(grid[0])
        if coord.y < 0 or coord.y >= col:
            return False
        if coord.x < 0 or coord.x >= row:
            return False
        if grid[coord.x][coord.y] == 1:
            return False
        return True

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not self.checkValid(grid, source):
            return -1
        if not self.checkValid(grid, destination):
            return -1
        step = 0
        queue = []
        queue.append(source)
        grid[source.x][source.y] = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                coord = queue.pop(0)
                if coord.x == destination.x and coord.y == destination.y:
                    return step
                for move_x, move_y in self.move:
                    p = Point(coord.x + move_x, coord.y + move_y)
                    if not self.checkValid(grid, p):
                        continue
                    queue.append(p)
                    grid[coord.x + move_x][coord.y + move_y] = 1
            step += 1
        return -1


"""
方法二：BFS distance hash 记录距离
"""
class Solution:

    directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

    """
    @param x: x coordinate
    @param y: y coordinate
    @param grid: a chessboard included 0 (false) and 1 (true)
    @return: True or False
    """
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return not grid[x][y]

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        queue = collections.deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return distance[(x, y)]
            for dx, dy in self.directions:
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in distance:
                    continue
                if not self.is_valid(next_x, next_y, grid):
                    continue
                distance[(next_x, next_y)] = distance[(x, y)] + 1
                queue.append((next_x, next_y))
        return -1


"""
方法三：双向BFS
使用bi-directional BFS的解法，优化时间复杂度。基本和单向的思路一模一样，
只是增加了两个方向，并且检查两个dict来看是否出现过，和自本方向的dict有
match的话，表明visit过；和相反方向的match的话，表明找到了。

基本思路：
1）建立两套queue + dict的组合
2）每次左边pop一个，右边pop一个，三个判断条件：
a.是否越界
b.是否在本方向dict里面
c.是否在对面方向的dict里面
"""
class Solution:

    directions = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

    """
    @param x: x coordinate
    @param y: y coordinate
    @param grid: a chessboard included 0 (false) and 1 (true)
    @return: True or False
    """
    def is_valid(self, x, y, grid):
        n, m = len(grid), len(grid[0])
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return not grid[x][y]

    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        qstart = collections.deque([(source.x, source.y)])
        qend = collections.deque([(destination.x, destination.y)])
        dstart = {(source.x, source.y): 0}
        dend = {(destination.x, destination.y): 0}

        while qstart and qend:
            xleft, yleft = qstart.popleft()
            xright, yright = qend.popleft()

            for dx, dy in self.directions:
                xnext, ynext = xleft + dx, yleft + dy
                if (xnext, ynext) in dstart:
                    continue
                if not self.is_valid(xnext, ynext, grid):
                    continue
                qstart.append((xnext, ynext))
                dstart[(xnext, ynext)] = dstart[(xleft, yleft)] + 1
                if (xnext, ynext) in dend:
                    return dstart[(xnext, ynext)] + dend[(xnext, ynext)]

            for dx, dy in self.directions:
                xnext, ynext = xright + dx, yright + dy
                if (xnext, ynext) in dend:
                    continue
                if not self.is_valid(xnext, ynext, grid):
                    continue
                qend.append((xnext, ynext))
                dend[(xnext, ynext)] = dend[(xright, yright)] + 1
                if (xnext, ynext) in dstart:
                    return dend[(xnext, ynext)] + dstart[(xnext, ynext)]

        return -1
