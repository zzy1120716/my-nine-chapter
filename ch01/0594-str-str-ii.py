"""
594. 字符串查找 II
实现时间复杂度为 O(n + m)的方法 strStr。
strStr 返回目标字符串在源字符串中第一次出现的
第一个字符的位置. 目标字串的长度为 m , 源字串
的长度为 n . 如果目标字串不在源字串中则返回 -1。

样例
给出 source = abcdef, target = bcd, 返回 1 .
"""
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        BASE = 1000000
        # write your code here
        # Rabin Karp
        if source is None or target is None:
            return -1
        
        m = len(target)
        n = len(source)
        
        if m == 0:
            return 0

        # 31 ^ m
        power = 1
        for i in range(m):
            # 一边乘一边取模，保证不越界
            power = (power * 31) % BASE

        targetCode = 0
        # 计算target的hash code
        for i in range(m):
            targetCode = (targetCode * 31 + ord(target[i])) % BASE

        hashCode = 0
        for i in range(n):
            # abc + d
            hashCode = (hashCode * 31 + ord(source[i])) % BASE
            
            if i < m - 1:
                continue

            # abcd - a
            if i >= m:
                hashCode = hashCode - (ord(source[i - m]) * power) % BASE
                if hashCode < 0:
                    hashCode += BASE

            # double check the string
            if hashCode == targetCode:
                if source[i - m + 1: i + 1] == target:
                    return i - m + 1

        return -1