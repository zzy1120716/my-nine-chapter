"""
154. 正则表达式匹配
实现支持'.'和'*'的正则表达式匹配。

'.'匹配任意一个字母。

'*'匹配零个或者多个前面的元素。

匹配应该覆盖整个输入字符串，而不仅仅是一部分。

需要实现的函数是：bool isMatch(string s, string p)

样例
isMatch("aa","a") → false

isMatch("aa","aa") → true

isMatch("aaa","aa") → false

isMatch("aa", "a*") → true

isMatch("aa", ".*") → true

isMatch("ab", ".*") → true

isMatch("aab", "c*a*b") → true
"""
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        match = self.dfs(s,p,0,0,{})
        return match 
        
    def dfs(self, s,p, sindex, pindex,memo):
        if (sindex,pindex) in memo:
            return memo[sindex,pindex]
        if (len(s) == 0  and len(p) != 0 ) or (len(p) == 0 and len(s) != 0 ) or p[0] == "*":
            return False
        
        if len(s) == sindex:
            sub = p[pindex:]
            for i in sub:
                if i == "*":
                    continue
                elif i != s[-1]:
                    return False
            return True    
                
        if len(p) == pindex:
            return sindex == len(s)
        
        match = False
        if p[pindex] == s[sindex]:
            match = self.dfs(s,p,sindex+1,pindex+1,memo)
        # 用来排除 c*a 和 ba 这种情况， wildcard 没有这种情况
        elif pindex+2 < len(p) and p[pindex+1] == "*" and p[pindex+2] == s[sindex]:
            match = self.dfs(s,p,sindex,pindex+2,memo)
        elif p[pindex] == ".":
            p[pindex] == s[sindex]
            match = self.dfs(s,p,sindex+1,pindex+1,memo)  
        elif p[pindex] == "*":
            match = self.dfs(s,p,sindex,pindex-1,memo) 
       
        else:
            match = False
        
        memo[sindex,pindex] = match 
        return match