"""
192. 通配符匹配
判断两个可能包含通配符“？”和“*”的字符串是否匹配。
匹配规则如下：

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个串完全匹配才算匹配成功。


函数接口如下:

bool isMatch(const char *s, const char *p)

样例
一些例子：

isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        return self.is_match_helper(s, 0, p, 0, {})
    
    # source 从 i 开始的后缀能否匹配上 pattern 从 j 开始的后缀
    def is_match_helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # source is empty
        if len(source) == i:
            # every character should be "*"
            for index in range(j, len(pattern)):
                if pattern[index] != '*':
                    return False
            return True
        
        if len(pattern) == j:
            return False
        
        if pattern[j] != '*':
            matched = self.is_match_char(source[i], pattern[j]) and self.is_match_helper(source, i + 1, pattern, j + 1, memo)
        else:
            matched = self.is_match_helper(source, i + 1, pattern, j, memo) or self.is_match_helper(source, i, pattern, j + 1, memo)
        
        memo[(i, j)] = matched
        return matched
    
    def is_match_char(self, s, p):
        return s == p or p == '?'