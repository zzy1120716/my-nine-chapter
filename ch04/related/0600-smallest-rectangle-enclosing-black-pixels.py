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
# 典型的BFS方法，超时
# 二分方法查看ch02 optional
from collections import deque


class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        image = self.convert(image)

        row, col = len(image), len(image[0])
        if row == 0 or col == 0:
            return -1

        left_top_most = Pixel(x, y)
        right_bottom_most = Pixel(x, y)

        q = deque([Pixel(x, y)])
        image[x][y] = 0
        while q:
            curr = q.popleft()
            for dx, dy in self.directions:
                nx = curr.x + dx
                ny = curr.y + dy

                if not self.in_bound(image, nx, ny) or image[nx][ny] == 0:
                    continue

                left_top_most.x = min(left_top_most.x, nx)
                left_top_most.y = min(left_top_most.y, ny)
                right_bottom_most.x = max(right_bottom_most.x, nx)
                right_bottom_most.y = max(right_bottom_most.y, ny)

                q.append(Pixel(nx, ny))
                image[nx][ny] = 0

        return (right_bottom_most.x - left_top_most.x + 1) * (right_bottom_most.y - left_top_most.y + 1)

    def in_bound(self, image, x, y):
        row, col = len(image), len(image[0])
        return 0 <= x < row and 0 <= y < col

    def convert(self, image):
        image_matrix = []
        for row in image:
            vector = []
            for c in row:
                vector.append(int(c))
            image_matrix.append(vector)
        return image_matrix


if __name__ == '__main__':
    print(Solution().minArea([
        "0010",
        "0110",
        "0100"
    ], 0, 2))
