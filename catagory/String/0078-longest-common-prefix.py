"""
78. 最长公共前缀
给k个字符串，求出他们的最长公共前缀(LCP)

样例
在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"
"""


class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""
        res = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[0: len(res) - 1]
        return res
