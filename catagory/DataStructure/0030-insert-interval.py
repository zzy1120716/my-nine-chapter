"""
30. 插入区间
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

样例
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].

Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
"""


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# 方法一：O(logn)
class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if len(intervals) == 0:
            return [newInterval]

        left = self.binarySearch(intervals, newInterval.start)
        right = self.binarySearch(intervals, newInterval.end)
        length = len(intervals)

        merge_left = left < length and intervals[left].end >= newInterval.start
        merge_right = right < length and intervals[right].start <= newInterval.end
        l = left if merge_left or left >= length else left + 1
        r = right + 1 if merge_right else right

        start = min(intervals[left].start, newInterval.start) if merge_left else newInterval.start
        end = max(intervals[right].end, newInterval.end) if merge_right else newInterval.end

        return intervals[:l] + [Interval(start, end)] + intervals[r:]

    def binarySearch(self, intervals, val):
        left, right = 0, len(intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid].start <= val <= intervals[mid].end:
                return mid
            elif val < intervals[mid].start:
                right = mid - 1
            else:
                left = mid + 1

        return left


# 方法二：O(n)
# 分三种情况：
# 1）新区间在当前区间之前
# 2）新区间在当前区间之后
# 3）新区间与当前区间有重叠
class Solution1:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        result = []
        insert_pos = 0
        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                result.append(intervals[i])
                insert_pos += 1
            elif intervals[i].start > newInterval.end:
                result.append(intervals[i])
            else:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.end = max(intervals[i].end, newInterval.end)
        result.insert(insert_pos, newInterval)
        return result


if __name__ == '__main__':
    intervals = [Interval(1, 2), Interval(5, 9)]
    newInterval1 = Interval(3, 4)
    newInterval2 = Interval(2, 5)
    results = Solution().insert(intervals, newInterval1)
    for res in results:
        print("(" + str(res.start) + "," + str(res.end) + ")")
    print("------------------------------------------------")
    results = Solution().insert(intervals, newInterval2)
    for res in results:
        print("(" + str(res.start) + "," + str(res.end) + ")")
    print("------------------------------------------------")
