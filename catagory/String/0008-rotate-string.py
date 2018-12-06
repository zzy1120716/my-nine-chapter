"""
8. 旋转字符串
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

样例
对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
挑战
在数组上原地旋转，使用O(1)的额外空间
"""


# 三步翻转法，注意边界条件，str为空、偏移量大于等于字符串长度
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        # edge cases
        if not str:
            return
        n = len(str)
        while offset >= n:
            offset %= n

        self.reverse(str, 0, n - offset - 1)
        self.reverse(str, n - offset, n - 1)
        self.reverse(str, 0, n - 1)

    def reverse(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1


# python数组切片操作
class Solution1:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if not str:
            return
        n = len(str)
        while offset >= n:
            offset %= n
        m = offset
        str[:-m] = str[:-m][::-1]
        str[-m:] = str[-m:][::-1]
        str[:] = str[:][::-1]
