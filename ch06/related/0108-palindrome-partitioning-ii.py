"""
108. 分割回文串 II
给定一个字符串s，将s分割成一些子串，使每个子串都是回文。

返回s符合要求的的最少分割次数。

样例
比如，给出字符串s = "aab"，

返回 1， 因为进行一次分割可以将字符串s分割成["aa","b"]这样两个回文子串
"""
import sys


# 方法一：DFS，DP 求出 isPalindrome 数组，再用 Memorized DFS 求最小切割数
class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        n = len(s)
        isPalindrome = [[False for j in range(n)] for i in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True

        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                if isPalindrome[i][j] and s[i - 1] == s[j + 1]:
                    isPalindrome[i - 1][j + 1] = True

        return self.dfs(s, n, 0, isPalindrome, {})

    def dfs(self, s, n, start, isPalindrome, records):
        if start >= len(s):
            return -1

        if start in records:
            return records[start]

        minCut = sys.maxsize
        for end in range(start, n):
            if isPalindrome[start][end]:
                cutsOfRest = self.dfs(s, n, end + 1, isPalindrome, records)
                minCut = min(minCut, cutsOfRest + 1)

        records[start] = minCut

        return minCut


# 方法二：DP
class Solution1:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        # write your code here
        n = len(s)
        f = []
        p = [[False for _ in range(n)] for _ in range(n)]
        # the worst case is cutting by each char
        for i in range(n + 1):
            f.append(n - 1 - i)  # the last one, f[n] = -1
        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]


if __name__ == '__main__':
    print(Solution1().minCut("aab"))
