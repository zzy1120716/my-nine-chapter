"""

10. 字符串的不同排列
给出一个字符串，找到它的所有排列，注意同一个字符串不要打印两次。

样例
给出 "abb"，返回 ["abb", "bab", "bba"]。

给出 "aabb"，返回 ["aabb", "abab", "baba", "bbaa", "abba", "baab"]。
"""
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        results = []
        str = ''.join(sorted(str))
        self.dfs(str, '', results)
        return results
    
    def dfs(self, str, seq, results):
        if not str:
            results.append(seq)
            return
        
        for i in range(len(str)):
            if i != 0 and str[i - 1] == str[i]:
                continue
            self.dfs(str[:i] + str[i + 1:], seq + str[i], results)