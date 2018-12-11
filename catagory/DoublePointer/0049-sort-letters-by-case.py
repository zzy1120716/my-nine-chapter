"""
49. 字符大小写排序
给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

样例
给出"abAcD"，一个可能的答案为"acbAD"

挑战
在原地扫描一遍完成

注意事项
小写字母或者大写字母他们之间不一定要保持在原始字符串中的相对位置。
"""


# 方法一：双指针
class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        start, end = 0, len(chars) - 1
        while start <= end:
            while start <= end and chars[start].islower():
                start += 1
            while start <= end and chars[end].isupper():
                end -= 1
            if start <= end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1
                end -= 1


# 方法二：sort
class Solution1:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # write your code here
        chars.sort(key=lambda c: c.isupper())
