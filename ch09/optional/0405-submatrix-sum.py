"""
405. 和为零的子矩阵
给定一个整数矩阵，请找出一个子矩阵，使得其数字之和等于0.输出答案时，请返回左上数字和右下数字的坐标。

样例
给定矩阵

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
返回 [(1,1), (2,2)]

挑战
O(n ^ 3) 时间复杂度。
"""


# 方法一：先计算每个子矩阵的和
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return

        result = [[0] * 2 for _ in range(2)]
        row = len(matrix)
        col = len(matrix[0])

        # compute the sum of submatrix
        mat_sum = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(row):
            for j in range(col):
                mat_sum[i + 1][j + 1] = matrix[i][j] + mat_sum[i + 1][j] + mat_sum[i][j + 1] - mat_sum[i][j]

        # find coordinate of submatrix which sum is 0
        for i in range(row):
            for j in range(i + 1, row + 1):
                # hash to storage diff
                h = {}
                for k in range(col + 1):
                    diff = mat_sum[j][k] - mat_sum[i][k]
                    if diff in h:
                        v = h[diff]
                        result[0][0] = i
                        result[0][1] = v
                        result[1][0] = j - 1
                        result[1][1] = k - 1
                        return result
                    else:
                        h[diff] = k

        return result


# 方法二：枚举矩阵的上边界top和下边界down，把上下边界之间的每一列都压缩为一个数字（求和），
# 然后就成了 subarray-sum 的问题了
class Solution1:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """

    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return

        row, col = len(matrix), len(matrix[0])
        for top in range(row):
            arr = [0] * col
            for down in range(top, row):
                prefix_hash = {0: -1}
                prefix_sum = 0
                for c in range(col):
                    arr[c] += matrix[down][c]
                    prefix_sum += arr[c]
                    if prefix_sum in prefix_hash:
                        return [(top, prefix_hash[prefix_sum] + 1), (down, c)]
                    prefix_hash[prefix_sum] = c

        return


if __name__ == '__main__':
    print(Solution1().submatrixSum([
        [1, 5, 7],
        [3, 7, -8],
        [4, -8, 9],
    ]))
