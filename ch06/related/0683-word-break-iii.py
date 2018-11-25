"""
683. 单词拆分 III
给出一个单词表和一条去掉所有空格的句子，根据给出的单词表添加空格,
返回可以构成的句子的数量, 保证构成的句子中所有的单词都可以在单词表中找到.

样例
给一个字符串 CatMat, 给出字典 ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"],
返回 3
我们可以构成一下 3 条语句: CatMat = Cat Mat CatMat = Ca tM at CatMat = C at Mat

注意事项
忽略大小写
"""


# 方法一：动态规划，状态 f[i] 代表子串 s[:i-1] 能被分割成多少个句子。
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        if not s or not dict:
            return 0

        dict_lower = [word.lower() for word in dict]

        n = len(s)

        # define f[i]: number of sentences that s[:i - 1] can be
        # breaked into using words in dict
        f = [0 for _ in range(n + 1)]

        # init
        f[0] = 1

        # function
        for i in range(1, n + 1):
            for j in range(0, i):
                if s[j:i].lower() in dict_lower:
                    f[i] += f[j]

        # ans
        return f[-1]


# 方法二：记忆化搜索DFS
class Solution1:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # count max length of dict word and turn dict into lowercase
        max_len = 0
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
            if len(word) > max_len:
                max_len = len(word)

        return self.dfs(len(s), s.lower(), lower_dict, max_len, 0, {})

    def dfs(self, n, lower_s, lower_dict, max_len, start, records):
        if start == n:
            return 1

        if start in records:
            return records[start]

        count = 0
        for end in range(start + 1, min(n + 1, start + 1 + max_len)):
            if lower_s[start:end] in lower_dict:
                count += self.dfs(n, lower_s, lower_dict, max_len, end, records)

        records[start] = count

        return count


# 另一种记忆化搜索
class Solution2:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        lower_dict = []
        max_length = 0
        for d in dict:
            lower_dict.append(d.lower())
            max_length = max(max_length, len(d))
        return self.dfs(s.lower(), lower_dict, max_length, {})

    def dfs(self, s, dict, max_length, memo):
        if len(s) == 0:
            return 1
        if s in memo:
            return memo[s]
        count = 0
        for i in range(1, max_length+1):
            if i > len(s):
                break;
            word = s[:i]
            if word not in dict: continue
            count += self.dfs(s[i:], dict, max_length, memo)
        memo[s] = count
        return count


if __name__ == '__main__':
    print(Solution1().wordBreak3("CatMat", ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]))