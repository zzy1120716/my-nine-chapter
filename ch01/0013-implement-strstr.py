"""
13. 字符串查找
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出
target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

样例
如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

挑战
O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）

说明
在面试中我是否需要实现KMP算法？

不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。
当然你需要先跟面试官确认清楚要怎么实现这个题。
"""

"""
方法一：Brutal Force
"""
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        for i in range(len(source) - len(target) + 1):
            j = 0
            while j < len(target):
                if source[i + j] != target[j]:
                    break
                j += 1

            if j == len(target):
                return i

        return -1


"""
方法二：KMP （不用掌握）
"""
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0
        len_s = len(source)
        len_t = len(target)
        next = self.getNext(target)
        i = j = 0
        while i < len_s:
            if j == -1 or target[j] == source[i]:
                j += 1
                i += 1
                if j == len_t:
                    return i - j
            else:
                j = next[j]
        return -1

    def getNext(self, target):
        next = []
        next.append(-1)
        length = len(target)
        j, k = 0, -1
        while j < length - 1:
            if k == -1 or target[j] == target[k]:
                j += 1
                k += 1
                next.append(k)
            else:
                k = next[k]
        return next


"""
方法三：Robin Karp 见 strStr-ii
"""