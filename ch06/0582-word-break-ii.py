"""
582. 单词拆分II
给一字串s和单词的字典dict,在字串中增加空格来构建一个句子，
并且所有单词都来自字典。
返回所有有可能的句子。

样例
给一字串lintcode,字典为["de", "ding", "co", "code", "lint"]
则结果为["lint code", "lint co de"]。
"""
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})
    
    # 找到 s 的所有切割方案并 return
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        
        partitions = []
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
        
        if s in wordDict:
            partitions.append(s)
        
        memo[s] = partitions
        return partitions