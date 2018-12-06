"""
32. 最小子串覆盖
给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。

样例
给出source = "ADOBECODEBANC"，target = "ABC" 满足要求的解  "BANC"

挑战
要求时间复杂度为O(n)

说明
Should the characters in minimum window has the same order in target?
Not necessary.

注意事项
If there is no such window in source that covers all characters in target, return the emtpy string "".
If there are multiple such windows, you are guaranteed that there will always be only one unique minimum
window in source.
The target string may contain duplicate characters, the minimum window should cover all characters including the
duplicate characters in target.
"""
import collections
import sys


# 双指针sliding window
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        cnt = collections.defaultdict(int)
        for c in target:
            cnt[c] += 1

        start, total, min_len, j = 0, len(target), sys.maxsize, 0

        for i in range(len(source)):
            if cnt[source[i]] > 0:
                total -= 1
            cnt[source[i]] -= 1

            while total == 0:
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    start = j
                cnt[source[j]] += 1
                if cnt[source[j]] > 0:
                    total += 1
                j += 1

        return source[start:start + min_len] if min_len != sys.maxsize else ""


# 将defaultdict改为list，提高效率
class Solution1:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        cnt = [0] * 128
        for c in target:
            cnt[ord(c)] += 1

        start, total, min_len, j = 0, len(target), sys.maxsize, 0

        for i in range(len(source)):
            if cnt[ord(source[i])] > 0:
                total -= 1
            cnt[ord(source[i])] -= 1

            while total == 0:
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    start = j
                cnt[ord(source[j])] += 1
                if cnt[ord(source[j])] > 0:
                    total += 1
                j += 1

        return source[start:start + min_len] if min_len != sys.maxsize else ""


if __name__ == '__main__':
    print(Solution1().minWindow("ADOBECODEBANC", "ABC"))
