"""
53. 翻转字符串中的单词
给定一个字符串，逐个翻转字符串中的每个单词。

说明
单词的构成：无空格字母构成一个单词
输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
"""


# 方法一：采用python内置函数
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        return ' '.join(reversed(s.strip().split()))


# 方法二：自行实现
class Solution1:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        arr = list(s)
        self.reverse_string(arr, 0, len(arr) - 1)
        self.reverse_word(arr)
        word = self.trim_sides(arr)
        res = self.trim_space(word)
        return ''.join(res)

    def reverse_string(self, arr, l, r):
        """reverse a given string"""
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

    def reverse_word(self, arr):
        """reverse every words in a string"""
        l, r = 0, 0
        while r < len(arr):
            while r < len(arr) and not arr[r].isspace():
                r += 1
            self.reverse_string(arr, l, r - 1)
            r += 1
            l = r
        return arr

    def trim_sides(self, arr):
        """str.strip() basically"""
        if ''.join(arr).isspace():
            return []
        l, r = 0, len(arr) - 1
        while l < r and arr[l].isspace():
            l += 1
        while l < r and arr[r].isspace():
            r -= 1
        return arr[l:r + 1]

    def trim_space(self, word):
        """remove duplicating space in a word"""
        if not word:
            return []
        res = [word[0]]
        for i in range(1, len(word)):
            if res[-1].isspace() and word[i].isspace():
                continue
            res.append(word[i])
        return res
