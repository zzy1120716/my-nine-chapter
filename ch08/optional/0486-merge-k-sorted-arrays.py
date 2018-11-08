"""
486. Merge K Sorted Arrays
将 k 个排序数组合并为一个大的排序数组。

样例
给出下面的 3 个排序数组：

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
合并后的大数组应为：

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
挑战
在 O(N log k) 的时间复杂度内完成：

N 是所有数组包含的整数个数。
k 是数组的个数。
"""


# 方法一：利用堆，适合海量数据处理
import heapq


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        res, heap = [], []

        # 将每个数组中的第一个元素push进堆
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], array, 1))

        # 每一轮pop一个最小值，并把同一数组的下一个值push入堆
        while len(heap):
            val, arr, next_idx = heap[0]
            heapq.heappop(heap)
            res.append(val)
            if next_idx < len(arr):
                heapq.heappush(heap, (arr[next_idx], arr, next_idx + 1))

        return res


# 方法二：两两归并
class Solution1:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if not arrays or len(arrays) == 0:
            return []
        if len(arrays) == 1:
            return arrays[0]

        mid = len(arrays) // 2
        left = self.mergekSortedArrays(arrays[mid:])
        right = self.mergekSortedArrays(arrays[:mid])
        return self.mergeSort(left, right)

    def mergeSort(self, arr1, arr2):
        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1
        while j < len(arr2):
            res.append(arr2[j])
            j += 1

        return res


if __name__ == '__main__':
    ans = Solution1().mergekSortedArrays([
        [1, 3, 5, 7],
        [2, 4, 6],
        [0, 8, 9, 10, 11]
    ])
    print(ans)