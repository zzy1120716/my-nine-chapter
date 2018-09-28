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
        q = Queue(maxsize = n * m)
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