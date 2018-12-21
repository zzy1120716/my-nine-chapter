"""
125. 背包问题 II
给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？

样例
对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。

挑战
O(n x m) memory is acceptable, can you do it in O(m) memory?

注意事项
A[i], V[i], n, m均为整数。你不能将物品进行切分。你所挑选的物品总体积需要小于等于给定的m。
"""


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] > j:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i - 1]] + V[i - 1])
        
        return f[-1][-1]


if __name__ == '__main__':
    print(Solution().backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4]))
