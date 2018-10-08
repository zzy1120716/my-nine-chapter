"""
577. 合并K个排序间隔列表
将K个排序的间隔列表合并到一个排序的间隔列表中，你需要合并重叠的间隔。

样例
给定：

[
  [(1,3),(4,7),(6,8)],
  [(1,2),(9,10)]
]
返回

[(1,3),(4,8),(9,10)]
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
方法一：利用第839题合并两区间list，归并
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
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals[0]

        mid = len(intervals) // 2
        left = self.mergeKSortedIntervalLists(intervals[:mid])
        right = self.mergeKSortedIntervalLists(intervals[mid:])

        return self.mergeTwo(left, right)

    def mergeTwo(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2

        res = []
        i, j, last, curr = 0, 0, None, None
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                curr = list1[i]
                i += 1
            else:
                curr = list2[j]
                j += 1
            last = self.merge(res, curr, last)

        while i < len(list1):
            last = self.merge(res, list1[i], last)
            i += 1
        while j < len(list2):
            last = self.merge(res, list2[j], last)
            j += 1

        if last:
            res.append(last)

        return res

    def merge(self, res, curr, last):
        if last is None:
            return curr

        if curr.start > last.end:
            res.append(last)
            return curr

        last.end = max(curr.end, last.end)
        return last


"""
方法二：heap
"""
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        import heapq
        data, res, last = [], [], None
        for interval_list in intervals:
            for interval in interval_list:
                heapq.heappush(data, (interval.start, interval.end))

        while data:
            curr = heapq.heappop(data)
            curr = Interval(curr[0], curr[1])
            if not last or last.end < curr.start:
                res += [curr]
                last = curr
            elif last.end > curr.end:
                continue
            else:
                last.end = curr.end
        return res


"""
方法三：sort function
"""
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        data = []
        for interval_list in intervals:
            data += interval_list
        # 按start由小到大排序
        data.sort(key = lambda t:t.start)
        res = [data[0]]
        for curr in data:
            if res[-1].end < curr.start:
                res += [curr]
            else:
                res[-1].end = max(res[-1].end, curr.end)
        return res