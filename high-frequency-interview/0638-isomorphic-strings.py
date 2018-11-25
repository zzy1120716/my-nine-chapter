"""
638. Isomorphic Strings
给定两个字符串 s 和 t ，确定它们是否是同构的。
两个字符串是同构的如果 s 中的字符可以被替换得到 t。
所有出现的字符必须用另一个字符代替，同时保留字符串的顺序。 没有两个字符可以映射到同一个字符，但一个字符可以映射到自己。

样例
给出 s = "egg", t= "add", 返回 true。
给出 s = "foo", t= "bar", 返回 false。
给出 s = "paper", t= "title", 返回 true。

注意事项
你可以假定两个字符串 s 和 t 是一样长度的.
"""


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            elif d1[s[i]] != t[i]:
                return False

        for j in range(len(t)):
            if t[j] not in d2:
                d2[t[j]] = s[j]
            elif d2[t[j]] != s[j]:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic("egg", "add"))
    print(Solution().isIsomorphic("foo", "bar"))
    print(Solution().isIsomorphic("paper", "title"))
