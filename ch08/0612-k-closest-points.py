"""
612. K个最近的点
给定一些 points 和一个 origin，从 points 中找到 k 个
离 origin 最近的点。按照距离由小到大返回。如果两个点
有相同距离，则按照x值来排序；若x值也相同，就再按照y值
排序。

样例
给出 points = [[4,6],[4,7],[4,4],[2,5],[1,1]],
origin = [0, 0], k = 3
返回 [[1,1],[2,5],[4,4]]
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq


class Type:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def cmp(self, other):
        if other.dist != self.dist:
            return other.dist - self.dist
        if other.point.x != self.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __eq__(self, other):
        return self.cmp(other) == 0


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, Type(dist, point))
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while len(self.heap) > 0:
            ret.append(heapq.heappop(self.heap).point)

        ret.reverse()
        return ret

    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
