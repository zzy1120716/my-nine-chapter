"""
841. 字符串替换
给定两个相同大小的字符串数组 A 和 B，再给一个字符串 S，所有出现在 S 里的子串 A
都要替换成 B。(注意：从左往右，能替换的必须替换，如果有多种替换方案，替换更长的优先。
替换后的字符不能再做替换)

样例
给出 A = ["ab","aba"] , B = ["cc","ccc"] , S = "ababa" , 返回 "cccba"。

按照规则，从左往右能替换的是“ab”或者“aba”,由于“aba”替换的更长，故将”aba”
替换为”ccc”。
给出 A = ["ab","aba"] , B = ["cc","ccc"] , S = "aaaaa" , 返回 "aaaaa"。

S中没有包含A中的字符串，故不做替换。
给出 A = ["cd","dab","ab"], B = ["cc","aaa","dd"], S = "cdab", 返回 "ccdd"。

从左往右，最开始可以发现"cd"可以被替换，故替换后变成了"ccab",接下来可以发现"ab"可以
被替换，故替换后的字符串为"ccdd"。

注意事项
每个字符串数组的大小不超过100,总字符串长度不超过50000。
A[i] 和B[i]的长度相等。
S的长度不超过50000。
所有字符均为小写字母。
保证A数组没有相同的字符串
"""

"""
方法一：暴力法
优化以下几点：
1) 遍历时只找可能的替换字符串长度
2) 用dict存储替换字符串的index
"""
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # Write your code here
        repLens = set()
        idxMap = {}
        for i in range(len(a)):
            repLens.add(len(a[i]))
            idxMap[a[i]] = i

        repLens = sorted(repLens, reverse=True)

        result = ""
        start = 0
        while start < len(s):
            found = False
            for replen in repLens:
                end = start + replen
                if end > len(s):
                    continue

                str = s[start: end]
                if str in a:
                    result += b[idxMap[str]]
                    found = True
                    start = end
                    break

            if not found:
                result += s[start]
                start += 1

        return result