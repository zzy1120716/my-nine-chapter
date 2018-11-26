"""
828. 字模式
给定一个模式和一个字符串str，查找str是否遵循相同的模式。
这里遵循的意思是一个完整的匹配，在一个字母的模式和一个非空的单词str之间有一个双向连接的模式对应。

样例
给定模式= "abba"， str = "dog cat cat dog"，返回true。给定模式= "abba"， str = "dog cat cat fish"，返回false。
给定模式= "aaaa"， str = "dog cat cat dog"，返回false。给定模式= "abba"， str = "dog dog dog dog"，返回false。

注意事项
您可以假设模式只包含小写字母，而str包含由单个空间分隔的小写字母。
"""


# short solution from LeetCode
class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        str_list = teststr.split()
        return list(map(pattern.find, pattern)) == list(map(str_list.index, str_list))

    def wordPattern1(self, pattern, teststr):
        # write your code here
        f = lambda s: map({}.setdefault, s, range(len(s)))
        return list(f(pattern)) == list(f(teststr.split()))

    def wordPattern2(self, pattern, teststr):
        # write your code here
        s = pattern
        t = teststr.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)


# 用一个set保存不重复的字符串
class Solution1:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        word_map = {}
        # set用来预防：ab = "cat cat"这种情况
        unique_strs = set()
        str_list = teststr.split()

        # 如果长度不相等直接return False
        if len(pattern) != len(str_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in word_map:
                # 如果set中没有就代表此时的pattern和str都是新的，添加
                if str_list[i] not in unique_strs:
                    word_map[pattern[i]] = str_list[i]
                    unique_strs.add(str_list[i])
                # 如果set中存在，代表之前有的pattern已经表示了str，返回False
                else:
                    return False

            if str_list[i] != word_map[pattern[i]]:
                return False

        return True


# 用HashMap记录pattern - word对应关系。
# 如果key 存在，value不一样，退出；如果key不存在，value存在，退出
class Solution2:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, teststr):
        # write your code here
        h = {}
        strs = teststr.split()
        for i in range(len(pattern)):
            c = pattern[i]
            if c not in h:
                if strs[i] in h.values():
                    return False
                h[c] = strs[i]
            else:
                if strs[i] != h[c]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().wordPattern("aa", "bog bod"))
    print(Solution().wordPattern("abba", "dog cat cat dog"))
