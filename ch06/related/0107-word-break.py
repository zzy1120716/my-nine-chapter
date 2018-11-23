"""
107. 单词拆分 I
给定字符串 s 和单词字典 dict，确定 s 是否可以分成一个或多个以空格分隔的子串，
并且这些子串都在字典中存在。

样例
给出

s = "lintcode"

dict = ["lint","code"]

返回 true 因为"lintcode"可以被空格切分成"lint code"
"""
from collections import deque


# 方法一：BFS（参考#624移除子串），空间超了MLE
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not s:
            return True
        if not dict:
            return False

        q = deque([s])
        visited = {s}

        while q:
            curr = q.popleft()
            for word in dict:
                index = curr.find(word)
                while index != -1:
                    new_s = curr[0:index] + curr[index + len(word):]
                    if len(new_s) == 0:
                        return True
                    if new_s not in visited:
                        q.append(new_s)
                        visited.add(new_s)
                    index = curr.find(word, index + 1)

        return False


# BFS优化版本
# 对find next片段做优化（限制在dict的长度内寻找）
class Solution1:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        if not n:
            return True
        if not dict:
            return False

        # get max length in dict
        max_len = len(max(dict, key=len))
        if max_len == 0:
            return False

        # BFS
        q = deque([0])
        visited = {0}

        while q:
            start = q.popleft()
            for end in range(start + 1, min(start + 1 + max_len, n + 1)):
                if end in visited:
                    continue

                if s[start:end] in dict:
                    if end == n:
                        return True
                    q.append(end)
                    visited.add(end)

        return False


# 方法二：动态规划
class Solution2:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict:
            return len(s) == 0

        n = len(s)
        f = [False] * (n + 1)
        f[0] = True

        max_len = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if not f[i - j]:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break

        return f[n]


# 详细注释版
class Solution3:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict:
            return len(s) == 0

        max_len = len(max(dict, key=len))

        # 长度为n的单词，有 n + 1 个切割点，比如：_l_i_n_t_
        can_break = [False] * (len(s) + 1)

        # 当s长度为0时
        can_break[0] = True

        for i in range(1, len(can_break)):
            j = 1
            while j <= max_len and j <= i:
                # i - j 表示从 i 点开始往前 j 个点的位置
                string = s[i - j:i]
                # 如果此 string 在词典中，并且 string 之前的字符串可以拆分
                if string in dict and can_break[i - j]:
                    can_break[i] = True
                    break
                j += 1

        return can_break[-1]


# 方法三：DFS
# 1、根据dict中每一个单词，建立一个key为word首字母，values为list of words 的initialMap。
# 例如：(key)l, (value)lint, leet
# 2、DFS搜索s中是否存在以index 'start'为首字母的解法。
# DFS中，需要避免不必要的stack overflow的情况。如果以某一个s.charAt(i)为首字母，并且
# dict有且只存在一个单词可供break，则跳过这个单词，start += word.length(),直到找到有
# 一个以上单词可供break的情况。
# 举例：
# 在每次DFS中：
# s = "ohmylintcode", dict = ["lint", "leet", "oh", "my", "code"]
# initialMap = {'o':["oh"], 'm':["my"], 'l':["lint","leet"], "c":[code]}
# start = 0, "【o】hmylintcode", initialMap中["oh"] ==> start + 2 = 2
# start = 2, "oh【m】ylintcode", initialMap中["my"] ==> start + 2 = 4
# start = 4, "ohmy【l】intcode", initialMap中["lint","leet"] ==> break
# 然后从start = 4开始继续DFS。
class Solution4:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not dict:
            return len(s) == 0

        # prepare hash: (key)initial letter, (value)list of string in dict
        initial_map = {}
        for word in dict:
            if len(word) == 0:
                continue
            if word[0] not in initial_map:
                initial_map[word[0]] = []
            initial_map[word[0]].append(word)

        # DFS
        return self.dfs(s, 0, initial_map)

    def dfs(self, s, start, initial_map):
        # base cases
        if start >= len(s):
            return True
        if s[start] not in initial_map:
            return False

        # find the position that s has more than one way to break
        # to avoid stack overflow
        while start < len(s):
            if s[start] not in initial_map:
                return False
            # check if s has more than one way to break at position start
            choices = initial_map[s[start]]
            if len(choices) == 1:
                # has only one choice
                word = choices[0]
                check_word = s[start:start + len(word)]
                # check if current word is breakable
                if check_word == word:
                    start += len(word)
                else:
                    return False
            else:
                # has more than one choice
                break

        if start >= len(s):
            return True

        # DFS
        for word in initial_map[s[start]]:
            if start + len(word) > len(s):
                continue
            check_word = s[start:start + len(word)]
            if check_word == word:
                success = self.dfs(s, start + len(word), initial_map)
                if success:
                    return True

        return False


if __name__ == '__main__':
    print(Solution4().wordBreak("abcd", ["a", "b", "abc", "cd"]))
    print(Solution4().wordBreak("aaab", ["b", "aa"]))
