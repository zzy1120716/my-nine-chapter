"""
3. 统计数字
计算数字k在0到n中的出现的次数，k可能是0~9的一个值

样例
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
"""


class Solution:
    """
    @param k: An integer
    @param n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        # write your code here
        res = 0
        for i in range(n + 1):
            j = i
            while True:
                if j % 10 == k:
                    res += 1
                j //= 10
                if j == 0:
                    break
        return res


if __name__ == '__main__':
    print(Solution().digitCounts(1, 12))
