"""
606. 第K大的元素 II
找到数组中第K大的元素，N远大于K

样例
在数组 [9,3,2,4,8] 中, 第三大 的元素是 4。
在数组 [1,2,3,4,5] 中, 第一大 的元素是 5，第二大 的元素是 4，第三大 的元素是3等等。

注意事项
你可以改变数组中元素的位置
"""


# 基本方法：参考#5，快速选择
# 根据题目中的前提条件，采用堆的方法减少时间
# quick select只是期望是O(N), 并不是真正意义上的O(N)
# N 远大于k，说明logk的复杂度很小，我们可以采用Nlogk复杂度的算法。

# 方法一：利用python内置方法
class Solution:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        import heapq
        return heapq.nlargest(k, nums).pop()


# 方法二：依旧利用heapq，堆
class Solution1:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)