"""
120. 单词接龙
给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列

比如：
每次只能改变一个字母。
变换过程中的中间单词必须在字典中出现。
样例
给出数据如下：

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，
返回它的长度 5

注意事项
如果没有转换序列则返回0。
所有单词具有相同的长度。
所有单词都只包含小写字母。
"""

"""
方法一：分层遍历的BFS
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        # 记录访问过的单词的set
        visited = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance
            
                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)
        
        return 0
    
    
    # O(26 * L ^ 2)
    # L is the length of word
    # 获取所有与给出单词相差一个字母的单词的list
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            # 'abcdefghijklmnopqrstuvwxyz'
            import string
            for char in string.ascii_lowercase:
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


"""
方法二：不使用分层遍历，使用hash存储每个节点的距离
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        # hash 存储各节点的距离
        distance = {start: 1}
        
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
                
            for next_word in self.get_next_words(word):
                if next_word not in dict or next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
        return 0
    
    
    # O(26 * L ^ 2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            # 'abcdefghijklmnopqrstuvwxyz'
            import string
            for char in string.ascii_lowercase:
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


"""
方法三：利用 tuple 存储 distance
"""
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        wordLen = len(start)
        # deque中的元素为tuple类型
        queue = collections.deque([(start, 1)])
        
        while queue:
            curr = queue.popleft()
            currWord = curr[0]; currLen = curr[1]
            if currWord == end:
                return currLen
                
            for next_word in self.get_next_words(currWord):
                if next_word in dict:
                    queue.append((next_word, currLen + 1))
                    dict.remove(next_word)
        return 0
    
    
    # O(26 * L ^ 2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            # 'abcdefghijklmnopqrstuvwxyz'
            import string
            for char in string.ascii_lowercase:
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words