"""
81. 数据流中位数
数字是不断进入数组的，在每次添加一个新的数进入数组的同时返回当前新数组的中位数。

样例
持续进入数组的数的列表为：[1, 2, 3, 4, 5]，则返回[1, 1, 2, 2, 3]

持续进入数组的数的列表为：[4, 5, 1, 3, 2, 6, 0]，则返回 [4, 4, 4, 3, 3, 3, 3]

持续进入数组的数的列表为：[2, 20, 100]，则返回[2, 2, 20]

挑战
时间复杂度为O(nlogn)

说明
中位数的定义：

中位数是排序后数组的中间值，如果有数组中有n个数，则中位数为A[(n-1)/2]。
比如：数组A=[1,2,3]的中位数是2，数组A=[1,19]的中位数是1。
"""
from heapq import heappush, heappop


# 用 maxheap 保存左半部分的数，用 minheap 保存右半部分的数。
# 把所有的数一左一右的加入到每个部分。左边部分最大的数就一直都是 median。
# 这个过程中，可能会出现左边部分并不完全都 <= 右边部分的情况。
# 这种情况发生的时候，交换左边最大和右边最小的数即可。
class Solution:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians

    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heappush(self.maxheap, -value)
        else:
            heappush(self.minheap, value)

        if len(self.maxheap) == 0 or len(self.minheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))


if __name__ == '__main__':
    print(Solution().medianII([1, 2, 3, 4, 5]))
    print(Solution().medianII([4, 5, 1, 3, 2, 6, 0]))
    print(Solution().medianII([2, 20, 100]))
