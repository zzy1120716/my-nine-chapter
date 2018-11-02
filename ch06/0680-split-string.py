"""
680. 分割字符串
给一个字符串,你可以选择在一个字符或两个相邻
字符之后拆分字符串,使字符串由仅一个字符或两
个字符组成,输出所有可能的结果

样例
给一个字符串"123"
返回[["1","2","3"],["12","3"],["1","23"]]
"""


# 方法一：爬楼梯，Divide & Conquer
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """
    def splitString(self, s):
        # write your code here
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        result1 = self.splitString(s[1:])
        result2 = self.splitString(s[2:])
        result = []
        for r1 in result1:
            result.append([s[0]] + r1)
        for r2 in result2:
            result.append([s[:2]] + r2)
        return result


# 方法二：DFS
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        res = []
        self.dfs(res, [], s)
        return res
    
    def dfs(self, res, path, s):
        if s == "":
            res.append(path[:]) # important: use path[:] to clone it
            return
        
        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i+1])
                self.dfs(res, path, s[i+1:])
                path.pop()