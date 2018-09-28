"""
121. 单词接龙 II
给出两个单词（start和end）和一个字典，
找出所有从start到end的最短转换序列。

变换规则如下：

每次只能改变一个字母。
变换过程中的中间单词必须在字典中出现。
样例
给出数据如下：

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

返回

[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]
注意事项
所有单词具有相同的长度。
所有单词都只包含小写字母。
"""
from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        indexes = self.build_indexes(dict)
        
        distance = {}
        self.bfs(end, start, distance, indexes)
        
        results = []
        self.dfs(start, end, distance, indexes, [start], results)
        
        return results
        
    # 建立一个index，key是去掉一个字符之后的pattern，如'a%c'
    # value是满足这个pattern的所有单词，如{'abc', 'adc'}
    def build_indexes(self, dict):
        indexes = {}
        for word in dict:
            for i in range(len(word)):
                key = word[:i] + '%' + word[i + 1:]
                if key in indexes:
                    indexes[key].add(word)
                else:
                    indexes[key] = set([word])
        return indexes
    
    # 记录所有单词到end的距离
    def bfs(self, start, end, distance, indexes):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, indexes):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    # 获取包含所有下一个单词的list  
    def get_next_words(self, word, indexes):
        words = []
        for i in range(len(word)):
            key = word[:i] + '%' + word[i + 1:]
            for w in indexes.get(key, []):
                words.append(w)
        return words

    def dfs(self, curt, target, distance, indexes, path, results):
        if curt == target:
            results.append(list(path))
            return
        
        for word in self.get_next_words(curt, indexes):
            # 确保离end的distan越来越近
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, indexes, path, results)
            path.pop()