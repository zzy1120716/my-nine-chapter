"""
471. 最高频的K个单词
给一个单词列表，求出这个列表中出现频次最高的K个单词。

样例
给出单词列表：

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
如果 k = 3, 返回 ["code", "lint", "baby"]。
如果 k = 4, 返回 ["code", "lint", "baby", "yes"]。

挑战
用 O（n log k)的时间和 O(n) 的额外空间完成。

注意事项
你需要按照单词的词频排序后输出，越高频的词排在越前面。如果两个单词出现的次数相同，
则词典序小的排在前面。
"""

import collections
import heapq


# 方法一：最小堆，heapify
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        d = collections.Counter(words).items()
        data = [(-v, k) for k, v in d]
        heapq.heapify(data)
        return [heapq.heappop(data)[1] for _ in range(k)]


# 方法二：sort
class Solution1:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        d = collections.Counter(words).items()
        return [k for k, v in sorted(d, key=lambda x: (-x[1], x[0]))[:k]]


# 方法三：最大堆，data structure
class WordFreq:
    def __init__(self, count=0, word=''):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        else:
            return self.count > other.count


class Solution2:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        d = collections.Counter(words).items()
        data = [WordFreq(v, k) for k, v in d]
        heapq.heapify(data)
        return [heapq.heappop(data).word for _ in range(k)]


# 方法四：最小堆，heappush
class Solution3:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        d, res = collections.Counter(words).items(), []
        [heapq.heappush(res, (-v, k)) for k, v in d]
        return [heapq.heappop(res)[1] for _ in range(k)]


# 官方答案：dict
class Solution4:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        p = []
        for key, value in d.items():
            p.append((value, key))
        p.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for i in range(k):
            result.append(p[i][1])
        return result


if __name__ == '__main__':
    print(Solution().topKFrequentWords([
        "yes", "lint", "code",
        "yes", "code", "baby",
        "you", "baby", "chrome",
        "safari", "lint", "code",
        "body", "lint", "code"
    ], 3))
    print(Solution().topKFrequentWords([
        "yes", "lint", "code",
        "yes", "code", "baby",
        "you", "baby", "chrome",
        "safari", "lint", "code",
        "body", "lint", "code"
    ], 4))
