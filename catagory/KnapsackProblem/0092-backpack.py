"""
92. 背包问题
在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

样例
如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。

挑战
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

注意事项
你不可以将物品进行切割。
"""


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True

        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]

        for i in range(m, -1, -1):
            if f[n][i]:
                return i

        return 0


if __name__ == '__main__':
    print(Solution().backPack(11, [2, 3, 4, 7]))
    print(Solution().backPack(12, [2, 3, 4, 7]))
