"""
388. 第k个排列
中文English
给定 n 和 k，求n的全排列中字典序第k个排列.

样例
样例 1:

输入: n = 3, k = 4
输出: "231"
解释:
n = 3时, 全排列如下:
"123", "132", "213", "231", "312", "321"
样例 2:

输入: n = 1, k = 1
输出: "1"
挑战
O(n*k)很容易, 你可以做到O(n^2n
​2
​​ )或更低的时间复杂度吗?

注意事项
1 ≤ n ≤ 9
"""


class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # write your code here
        res = ""
        num = "123456789"
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            j = k // f[i - 1]
            k %= f[i - 1]
            res += num[j]
            num = num[:j] + num[j + 1:]
        return res


if __name__ == '__main__':
    print(Solution().getPermutation(4, 17))
