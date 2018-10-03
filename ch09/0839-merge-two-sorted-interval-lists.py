"""
839. 合并两个排序的间隔列表
合并两个已排序的间隔列表，并将其作为一个新的排序列表返回。
新的排序列表应该通过拼接两个列表的间隔并按升序排序。

样例
给定 list1 = [(1,2),(3,4)] 和 list2 = [(2,3),(5,6)],
返回 [(1,4),(5,6)].

注意事项
给定列表中的间隔一定不会重叠。
不同列表中的间隔可能会重叠。
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        i, j = 0, 0
        intervals = []
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(intervals, list1[i])
                i += 1
            else:
                self.push_back(intervals, list2[j])
                j += 1

        while i < len(list1):
            self.push_back(intervals, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(intervals, list2[j])
            j += 1

        return intervals

    """
    在intervals的末尾添加区间
    """
    def push_back(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = intervals[-1]
        if last_interval.end < interval.start:
            intervals.append(interval)
            return

        intervals[-1].end = max(intervals[-1].end, interval.end)