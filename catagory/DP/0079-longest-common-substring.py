"""
79. 最长公共子串
给出两个字符串，找到最长公共子串，并返回其长度。


样例
给出A=“ABCD”，B=“CBCE”，返回 2

挑战
O(n x m) time and memory.

注意事项
子串的字符应该连续的出现在原字符串中，这与子序列有所不同。
"""


# https://www.youtube.com/watch?v=BysNXJHzCEs
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        res = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res
