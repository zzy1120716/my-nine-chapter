"""
602. 俄罗斯套娃信封
给一定数量的信封，带有整数对 (w, h) 分别代表信封宽度和高度。一个信封的宽高均大于另一个
信封时可以放下另一个信封。
求最大的信封嵌套层数。

样例
给一些信封 [[5,4],[6,4],[6,7],[2,3]] ，最大的信封嵌套层数是 3([2,3] => [5,4] => [6,7])。
"""


# 方法一：动态规划，转换为#76最长上升子序列
from functools import cmp_to_key
import bisect


class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        if not envelopes or not envelopes[0] or len(envelopes[0]) != 2:
            return 0

        def mycmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            return a[0] - b[0]

        envelopes.sort(key=cmp_to_key(mycmp))

        dp = [0] * len(envelopes)
        length = 0
        for envelope in envelopes:
            index = bisect.bisect_left(dp, envelope[1], 0, length)
            dp[index] = envelope[1]
            if index == length:
                length += 1

        return length


# 方法二：官方答案
class Solution1:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        height = [a[1] for a in sorted(envelopes, key=lambda x: (x[0], -x[1]))]
        dp = [0] * len(height)
        length = 0

        for h in height:
            i = bisect.bisect_left(dp, h, 0, length)
            dp[i] = h
            if i == length:
                length += 1

        return length


# 方法三：动态规划解法，经过一维数组对优化时间复杂度O(nlogn) 空间复杂度O(n)
# 手动二分查找
# 关键点是排序要先第一维升序，如果第一维相等则第二维降序
# 方便理解举个例子，信封排序后为 [2,14]，[4,18]，[6,4]，[6,2]，[12,15]
# b数组变化
# 第一轮 0 -> -inf
# 第二轮 0 -> -inf 1->14
# 第三轮 0 -> -inf 1->14 2->18
# 第四轮 0 -> -inf 1->4 2->18
# 第五轮 0 -> -inf 1->2 2->18
# 第六轮 0 -> -inf 1->2 2->15
# 直接返回b的最高位有效位即可
class Solution2:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        n = len(envelopes)
        if n == 0:
            return 0

        def mycmp(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            return a[0] - b[0]

        envelopes.sort(key=cmp_to_key(mycmp))

        b = [0] * (n + 1)
        b[0] = -float('inf')
        btop = 0
        for i in range(n):
            mid, start, end = 0, 0, btop
            while start + 1 < end:
                mid = (start + end) // 2
                if b[mid] < envelopes[i][1]:
                    start = mid
                else:
                    end = mid

            # env < start
            if b[start] > envelopes[i][1]:
                b[start] = envelopes[i][1]
                continue

            # env > end
            if b[end] < envelopes[i][1]:
                b[end + 1] = envelopes[i][1]
                btop += 1
                continue

            # start <= env <= end
            b[start + 1] = envelopes[i][1]

        return btop


if __name__ == '__main__':
    print(Solution2().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(Solution2().maxEnvelopes([[2, 14], [4, 18], [6, 4], [6, 2], [12, 15]]))
