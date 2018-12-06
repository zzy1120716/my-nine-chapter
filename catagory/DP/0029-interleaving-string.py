"""
29. 交叉字符串
给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。

样例
比如 s1 = "aabcc" s2 = "dbbca"

    - 当 s3 = "aadbbcbcac"，返回  true.

    - 当 s3 = "aadbbbaccc"， 返回 false.

挑战
要求时间复杂度为O(n^2)或者更好
"""


# DP
class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[0][0] = True

        # first column
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] and (s2[i - 1] == s3[i - 1])
        # first row
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] and (s1[i - 1] == s3[i - 1])

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) \
                           or (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    assert(Solution().isInterleave("ac", "b", "abc"))
    assert(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    assert(not Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
