"""
254. Drop Eggs
There is a building of n floors. If an egg drops from the k th floor or above, it will
break. If it's dropped from any floor below, it will not break.

You're given two eggs, Find k while minimize the number of drops for the worst case.
Return the number of drops in the worst case.

样例
Given n = 10, return 4.
Given n = 100, return 14.

说明
For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor.
But in this worst case (k = 10), you have to drop 10 times.

Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst
case (for example, k = 9) you have to drop 4 times.
"""
import sys


# 动态规划，MLE
class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        T = [[0] * (n + 1) for _ in range(3)]
        for i in range(n + 1):
            T[1][i] = i

        for f in range(1, n + 1):
            T[2][f] = sys.maxsize
            for k in range(1, f + 1):
                c = 1 + max(T[1][k - 1], T[2][f - k])
                if c < T[2][f]:
                    T[2][f] = c

        return T[2][n]


if __name__ == '__main__':
    print(Solution().dropEggs(100))  # 14
