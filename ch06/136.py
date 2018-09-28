"""
136. 分割回文串
给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。

返回s所有可能的回文串分割方案。

样例
给出 s = "aab"，返回

[
  ["aa", "b"],
  ["a", "a", "b"]
]
"""
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results
        
    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            # results.append(stringlist)
            results.append(list(stringlist))
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                # self.dfs(s[i:], stringlist + [prefix], results)
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()

    def is_palindrome(self, s):
        return s == s[::-1]