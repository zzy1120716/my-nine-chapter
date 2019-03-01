"""
381. 螺旋矩阵 II
中文English
给定一个数n, 生成一个包含1~n^2n
​2
​​ 的螺旋形矩阵.

(螺旋由外向内顺时针旋转, 可参照样例)

样例
样例 1:

输入: 2
输出:
[
  [1, 2],
  [4, 3]
]
样例 2:

输入: 3
输出:
[
  [ 1, 2, 3 ],
  [ 8, 9, 4 ],
  [ 7, 6, 5 ]
]
"""


# 方法一：模拟螺旋形, 依次填入.
# 定义x, y为当前应填入数字的位置, d标志该位置前进的方向.
# 初始x, y在左上角, 即第一个位置, d标志右方.
# 每填入一个数字, 根据方向移动(x, y), 如果移动后的位置超过了边界或者已经被填过, 则转弯.
# d转弯的顺序依次是: 右下左上. 直到填入了n*n个数字为止即可.
class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generateMatrix(self, n):
        # write your code here
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, d = 0, 0, 0

        matrix = [[0] * n for _ in range(n)]
        for i in range(1, n * n + 1):
            matrix[x][y] = i
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny]:
                d = (d + 1) % 4
            x += dx[d]
            y += dy[d]

        return matrix


# 方法二：循环展开
class Solution2:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generateMatrix(self, n):
        # write your code here
        if n == 0:
            return []
        matrix = [[0] * n for _ in range(n)]
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        direction, count = 0, 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n * n:
                return matrix
            direction = (direction + 1) % 4


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
    print(Solution().generateMatrix(4))
