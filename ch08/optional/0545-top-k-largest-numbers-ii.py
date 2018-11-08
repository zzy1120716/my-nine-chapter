"""
545. 前K大数 II
实现一个数据结构，提供下面两个接口
1.add(number) 添加一个元素
2.topk() 返回前K大的数

样例
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
"""


# 方法一：python中heapq的自带方法
import heapq
import sys


class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do initialization if necessary
        self.k = k
        self.nums = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.nums, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return heapq.nlargest(self.k, self.nums)


# 方法二：完全自主实现堆数据结构去维护前K个元素
class Solution1:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.size = k
        self.n = 0
        self.A = [-sys.maxsize for _ in range(k)]

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if self.n < self.size:
            self.offer(num)
        elif num > self.A[0]:
            self.poll()
            self.offer(num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        res = []
        for i in range(self.n):
            res.append(self.A[i])

        res.sort(reverse=True)
        return res

    def offer(self, num):
        self.A[self.n] = num
        self.n += 1
        k = self.n - 1

        while k > 0:
            p = (k - 1) // 2
            if self.A[k] < self.A[p]:
                self.A[k], self.A[p] = self.A[p], self.A[k]
            k = p

    def poll(self):
        self.A[0] = self.A[self.n - 1]
        self.n -= 1
        k = 0
        while k < self.n:
            left = 2 * k + 1
            right = 2 * k + 2
            min_index = k

            if left < self.n and self.A[left] < self.A[min_index]:
                min_index = left

            if right < self.n and self.A[right] < self.A[min_index]:
                min_index = right

            if min_index == k:
                break

            self.A[k], self.A[min_index] = self.A[min_index], self.A[k]
            k = min_index


if __name__ == '__main__':
    s = Solution1(3)
    s.add(3)
    s.add(10)
    print(s.topk())
    s.add(1000)
    s.add(-99)
    print(s.topk())
    s.add(4)
    print(s.topk())
    s.add(100)
    print(s.topk())