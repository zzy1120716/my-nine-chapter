"""
4. 丑数 II
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

样例
如果n = 9， 返回 10

挑战
要求时间复杂度为O(nlogn)或者O(n)

注意事项
我们可以认为1也是一个丑数
"""


# 方法一：使用heap，初始化min heap里面的值为1
# 做n次循环，每个从min heap pop出来的数乘以2，3，5
from heapq import heappush, heappop


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        heap = [1]
        visited = {1}

        val = None
        for i in range(n):
            val = heappop(heap)
            for multi in [2, 3, 5]:
                if val * multi not in visited:
                    visited.add(val * multi)
                    heappush(heap, val * multi)

        return val


# 方法二：维护3个position，计算分别乘以2,3,5后的最小值，加到list中
class Solution1:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        nums = [1]
        p1, p2, p3 = 0, 0, 0

        while len(nums) < n:
            v2 = nums[p1] * 2
            v3 = nums[p2] * 3
            v5 = nums[p3] * 5
            min_v = min(v2, v3, v5)
            if v2 == min_v:
                p1 += 1
            if v3 == min_v:
                p2 += 1
            if v5 == min_v:
                p3 += 1
            nums.append(min_v)

        return nums[-1]