"""
425. 电话号码的字母组合
Given a digit string excluded 01, return all possible 
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone 
buttons) is given below.

Cellphone

样例
给定 "23"

返回 ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

注意事项
以上的答案是按照词典编撰顺序进行输出的，不过，在做本题时，
你也可以任意选择你喜欢的输出顺序。
"""

KEYBOARD = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


# 方法一：DFS
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, '', results)
        return results
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return
        
        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)


# 方法二：BFS
class Solution1(object):

    def __init__(self):
        self.d2l = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        results = [""]
        for digit in digits:
            tmp = []
            for s in results:
                for c in self.d2l[digit]:
                    tmp.append(s + c)
            results = tmp
        return results


if __name__ == '__main__':
    print(Solution1().letterCombinations('23'))
