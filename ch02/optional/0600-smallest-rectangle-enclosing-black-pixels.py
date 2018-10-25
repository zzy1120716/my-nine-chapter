"""
600. 包裹黑色像素点的最小矩形
一个由二进制矩阵表示的图，0 表示白色像素点，1 表示黑色像素点。黑色像素点是联通的，
即只有一块黑色区域。像素是水平和竖直连接的，给一个黑色像素点的坐标 (x, y) ，返回囊
括所有黑色像素点的矩阵的最小面积。

样例
举个例子，给一个图

[
  "0010",
  "0110",
  "0100"
]
并且给出x = 0, y = 2, 则返回 6。
"""

"""
方法一：暴力法 O(m * n)
遍历找到上下左右四个方向最靠边界的黑像素点
"""
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        row, col = len(image), len(image[0])
        left = right = x
        top = bottom = y
        for i in range(row):
            for j in range(col):
                if image[i][j] == '1':
                    point = (i, j)
                    left = min(left, point[0])
                    right = max(right, point[0])
                    top = min(top, point[1])
                    bottom = max(bottom, point[1])
        return (right - left + 1) * (bottom - top + 1)


"""
方法二：二分查找 O(max(m,n)logmax(m,n))
"""
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        row, col = len(image), len(image[0])
        if not image or row == 0 or col == 0:
            return 0

        left = self.findLeft(image, 0, y)
        right = self.findRight(image, y, col - 1)
        top = self.findTop(image, 0, x)
        bottom = self.findBottom(image, x, row - 1)

        return (right - left + 1) * (bottom - top + 1)

    def findLeft(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.isEmptyCol(image, mid):
                start = mid
            else:
                end = mid
        if self.isEmptyCol(image, start):
            return end
        return start

    def findRight(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.isEmptyCol(image, mid):
                end = mid
            else:
                start = mid
        if self.isEmptyCol(image, end):
            return start
        return end

    def findTop(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.isEmptyRow(image, mid):
                start = mid
            else:
                end = mid
        if self.isEmptyRow(image, start):
            return end
        return start

    def findBottom(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.isEmptyRow(image, mid):
                end = mid
            else:
                start = mid
        if self.isEmptyRow(image, end):
            return start
        return end

    def isEmptyCol(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True

    def isEmptyRow(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return False
        return True


"""
方法三：BFS
会超时
"""
from queue import Queue

moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        row, col = len(image), len(image[0])
        if not image or row == 0 or col == 0:
            return 0

        minX = minY = sys.maxsize
        maxX = maxY = -sys.maxsize

        queue = Queue()
        queue.put(Pair(x, y))
        image[x][y] = 0

        while not queue.empty():
            curr = queue.get()
            minX = min(minX, curr.x)
            minY = min(minY, curr.y)
            maxX = max(maxX, curr.x)
            maxY = max(maxY, curr.y)

            for move in moves:
                nx = curr.x + move[0]
                ny = curr.y + move[1]

                if nx >= 0 and nx < row and ny >= 0 and ny < col and image[nx][ny] == '1':
                    queue.put(Pair(nx, ny))
                    image[nx][ny] = 0

        return (maxX - minX + 1) * (maxY - minY + 1)