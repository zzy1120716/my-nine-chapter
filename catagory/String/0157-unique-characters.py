"""
157. 判断字符串是否没有重复字符
实现一个算法确定字符串中的字符是否均唯一出现

样例
给出"abc"，返回 true

给出"aab"，返回 false

挑战
如果不使用额外的存储空间，你的算法该如何改变？
"""


class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        return len(list(set(str))) == len(str)


class Solution1:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        # write your code here
        char_set = [False for _ in range(256)]
        for c in str:
            if char_set[ord(c)]:
                return False
            char_set[ord(c)] = True
        return True
