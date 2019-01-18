"""
156. 合并区间
给出若干闭合区间，合并所有重叠的部分。

样例
给出的区间列表 => 合并后的区间列表：

[                     [
  (1, 3),               (1, 6),
  (2, 6),      =>       (8, 10),
  (8, 10),              (15, 18)
  (15, 18)            ]
]
挑战
O(n log n) 的时间和 O(1) 的额外空间。
"""


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# 先按区间的start从小到大排序
# 创建一个新数组，依次向新数组中添加区间，若：
# 1）新数组中的最后一个区间的end小于要添加区间的start，将两个区间合并，end值为二者end中的最大值；
# 2）新数组中的最后一个区间的end大于等于要添加区间的start，或新数组为空，直接添加。
class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        intervals = sorted(intervals, key=lambda x: x.start)
        results = []
        for interval in intervals:
            if len(results) == 0 or results[-1].end < interval.start:
                results.append(interval)
            else:
                results[-1].end = max(results[-1].end, interval.end)
        return results
