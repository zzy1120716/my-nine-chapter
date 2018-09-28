"""
667. 最长的回文序列
给一字符串 s, 找出在 s 中的最长回文序列的长度.
你可以假设 s 的最大长度为 1000.

样例
给出 s = bbbab 返回 4
一个可能的最长回文序列为 bbbb
"""
# 动态规划求解最长回文序列
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        length = len(s)
        if length == 0:
            return 0
    
        dp = [[0 for _ in range(length)] for __ in range(length)]
        for i in range(length - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][length - 1]