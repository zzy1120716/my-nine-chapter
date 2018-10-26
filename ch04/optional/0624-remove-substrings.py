"""
624. 移除子串
给出一个字符串 s 以及 n 个子串。你可以从字符串 s 中移除 n 个子串中的任意一个，
使得剩下来s的长度最小，输出这个最小长度。

样例
给出s = ccdaabcdbb，子串为 ["ab","cd"]
返回 2.

解释:
ccdaabcdbb -> ccdacdbb -> cabb -> cb (长度为 2)
"""

"""
方法一：BFS
使用一个集合记录访问过的字符串
"""
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        from queue import Queue
        queue = Queue()
        queue.put(s)
        visited = set([s])
        min_len = len(s)

        # 注意Queue的判空操作，与一般不同
        while not queue.empty():
            s = queue.get()
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found + len(sub):]
                    if new_s not in visited:
                        min_len = min(min_len, len(new_s))
                        queue.put(new_s)
                        visited.add(new_s)
                    found = s.find(sub, found + 1)

        return min_len

# 使用deque版本，熟悉队列相关操作
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        from collections import deque
        queue = deque([s])
        visited = set([s])
        min_len = len(s)

        while queue:
            s = queue.popleft()
            for sub in dict:
                found = s.find(sub)
                while found != -1:
                    new_s = s[:found] + s[found + len(sub):]
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
                        min_len = min(min_len, len(new_s))
                    found = s.find(sub, found + 1)

        return min_len


"""
方法二：DFS
"""
# TODO
