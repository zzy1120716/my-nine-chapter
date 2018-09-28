"""
627. 最长回文串
给出一个包含大小写字母的字符串。求出由这些字母
构成的最长的回文串的长度是多少。

数据是大小写敏感的，也就是说，"Aa" 并不会被认为
是一个回文串。

样例
给出 s = "abccccdd" 返回 7

一种可以构建出来的最长回文串方案是 "dccaccd"。

注意事项
假设字符串的长度不会超过 1010。
"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        hash = {}
        for c in s:
            if c in hash:
                del hash[c]
            else:
                hash[c] = True

        remove = len(hash)
        if remove > 0:
            remove -= 1

        return len(s) - remove

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))