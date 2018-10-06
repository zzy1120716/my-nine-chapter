"""
944. Maximum Submatrix
Given an n x n matrix of positive and negative integers,
find the submatrix with the largest possible sum.

样例
Given matrix =
[
[1,3,-1],
[2,3,-2],
[-1,-2,-3]
]
return 9.
Explanation:
the submatrix with the largest possible sum is:
[
[1,3],
[2,3]
]
"""

"""
将二维数组转化为有前缀和的一维数组
"""

class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """

    def maxSubmatrix(self, matrix):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return 0
        if matrix[0] is None or len(matrix[0]) == 0:
            return 0

        self.row = len(matrix)
        self.col = len(matrix[0])

        # prefix sum between row and row
        prefix_sum = self.getPrefixSum(matrix)
        max_sum = - sys.maxsize

        for up in range(self.row):
            for down in range(up, self.row):
                arr = self.compression(matrix, up, down, prefix_sum)
                max_sum = max(max_sum, self.maximumSubarray(arr))

        return max_sum

    def getPrefixSum(self, matrix):
        sum = [[0 for i in range(self.col)] for j in range(self.row + 1)]

        for i in range(self.col):
            for j in range(self.col):
                sum[i + 1][j] = sum[i][j] + matrix[i][j]

        return sum

    def compression(self, matrix, up, down, prefix_sum):
        arr = [0 for i in range(self.col)]
        for i in range(self.col):
            arr[i] = prefix_sum[down + 1][i] - prefix_sum[up][i]

        return arr

    def maximumSubarray(self, arr):
        temp_max = - sys.maxsize
        temp_min = 0
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            if sum < temp_min:
                temp_min = sum
            if sum - temp_min > temp_max:
                temp_max = sum - temp_min

        return temp_max