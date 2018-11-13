"""
611. 骑士的最短路线
给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空
1 表示有障碍物)，找到到达 终点 的最短路线，返回路线的
长度。如果骑士不能到达则返回 -1 。

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
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    deltaX = [1, 1, 2, 2, -1, -1, -2, -2]
    deltaY = [2, -2, 1, -1, 2, -2, 1, -1]
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        
        n = len(grid)
        m = len(grid[0])
        
        from queue import Queue
        q = Queue(maxsize=n * m)
        q.put(source)
        
        steps = 0
        while not q.empty():
            size = q.qsize()
            for i in range(0, size):
                point = q.get()
                if point.x == destination.x and point.y == destination.y:
                    return steps
                
                direction = 0
                for direction in range(0, 8):
                    nextPoint = Point(
                        point.x + self.deltaX[direction],
                        point.y + self.deltaY[direction]
                    )
                    
                    if not self.inBound(nextPoint, grid):
                        continue
                    
                    q.put(nextPoint)
                    
                    grid[nextPoint.x][nextPoint.y] = True
                    
            steps += 1
        return -1
    
    def inBound(self, point, grid):
        n = len(grid)
        m = len(grid[0])
        if point.x < 0 or point.x >= n:
            return False
        if point.y < 0 or point.y >= m:
            return False
        return grid[point.x][point.y] == False