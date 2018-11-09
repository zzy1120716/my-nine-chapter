"""
817. 范围矩阵元素和-可变的
给定一个2D数组矩阵，找出它的左上角(row1, col1)和右下角(row2, col2)定义的矩形内所有元素
的和

样例
给定矩阵=[
	[3, 0, 1, 4, 2],
	[5, 6, 3, 2, 1],
	[1, 2, 0, 1, 5],
	[4, 1, 0, 1, 7],
	[1, 0, 3, 0, 5]
]
元素和(2, 1, 4, 3) -> 8
更新(3,2,2)
元素和(2, 1, 4, 3) -> 10
注意事项
1.该矩阵仅可通过更新函数进行修改。
2.您可以假设更新和sumRegion函数的调用数量是均匀分布的。
3.你可以认定row1 ≤ row2 并且 col1 ≤ col2。
"""


# 方法一：Binary Indexed Tree
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.arr = [[0 for _ in range(self.m)] for _ in range(self.n)]
        self.bit = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]

        for i in range(self.n):
            for j in range(self.m):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[row][col]
        self.arr[row][col] = val

        i = row + 1
        while i <= self.n:
            j = col + 1
            while j <= self.m:
                self.bit[i][j] += delta
                j += self.lowbit(j)
            i += self.lowbit(i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return \
            self.prefixSum(row2, col2) - \
            self.prefixSum(row2, col1 - 1) - \
            self.prefixSum(row1 - 1, col2) + \
            self.prefixSum(row1 - 1, col1 - 1)

    def prefixSum(self, row, col):
        pre_sum = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                pre_sum += self.bit[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return pre_sum

    def lowbit(self, x):
        return x & (-x)


# 方法二：prefix_sum
# initialize 一个 prefix_sum
# prefix_sum里每一个点存的是当前列 （0,col -> row,col） 的和
# 这样，rangeSum就是O(n), update就是O(m)
class NumMatrix1(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.prefix_sum = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    self.prefix_sum[i][j] = matrix[i][j]
                else:
                    self.prefix_sum[i][j] = matrix[i][j] + self.prefix_sum[i-1][j]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(row, len(self.matrix)):
            self.prefix_sum[i][col] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for j in range(col1, col2+1):
            if row1 > 0:
                ans += (self.prefix_sum[row2][j] - self.prefix_sum[row1-1][j])
            else:
                ans += self.prefix_sum[row2][j]

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col


if __name__ == '__main__':
    nm = NumMatrix1([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])
    print(nm.sumRegion(2, 1, 4, 3))
    nm.update(3, 2, 2)
    print(nm.sumRegion(2, 1, 4, 3))
