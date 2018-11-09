"""
793. 多个数组的交集
给出多个数组，求它们的交集。输出他们交集的大小。

样例
给出 [[1,2,3],[3,4,5],[3,9,10]]，返回 1。

解释：
只有元素3在所有的数组中出现过。交集为[3]，大小为1。
给出 [[1,2,3,4],[1,2,5,6,7],[9,10,1,5,2,3]]，返回2。

解释：
只有元素1,2均在所有的数组出现过。交集为[1,2]，大小为2。
注意事项
输入的所有数组元素总数不超过500000。
题目数据每个数组里的元素没有重复。
"""


# 方法一：利用set自带方法
class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        if not arrs:
            return 0
        if len(arrs) == 1:
            return len(arrs[0])

        intersection = set(arrs[0])
        for i in range(1, len(arrs)):
            intersection &= set(arrs[i])

        return len(intersection)


# 方法二：官方答案，利用hash
class Solution1:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        h = {}
        for arr in arrs:
            for num in arr:
                if num in h:
                    h[num] += 1
                else:
                    h[num] = 1

        ans = 0
        for num, cnt in h.items():
            if cnt == len(arrs):
                ans += 1
        return ans


# 方法三：分治法
import collections


class Solution2:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        res = self.dc(arrs)
        return len(res)

    # divide & conquer
    def dc(self, arrs):
        if len(arrs) == 0:
            return []
        if len(arrs) == 1:
            return arrs[0]
        mid = len(arrs) // 2
        left = self.dc(arrs[:mid])
        right = self.dc(arrs[mid:])
        return self.intersectionOfTwo(left, right)

    def intersectionOfTwo(self, arr1, arr2):
        if not arr1 or not arr2:
            return []
        res = []
        c1 = collections.Counter(arr1)
        c2 = collections.Counter(arr2)
        c = c1 & c2
        for num, cnt in c.items():
            res += [num] * cnt
        return res


# 方法四：优先队列
from heapq import heappush, heappop


class Solution3:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        # write your code here
        if not arrs or len(arrs) == 0:
            return 0

        min_heap = []
        for i in range(len(arrs)):
            if not arrs[i] or len(arrs[i]) == 0:
                return 0
            arrs[i].sort()
            heappush(min_heap, (arrs[i][0], i, 0))

        lastValue, count = 0, 0
        result = 0
        while min_heap:
            cur_item = heappop(min_heap)
            if cur_item[0] != lastValue or count == 0:
                # if count == len(arrs):
                #     result += 1
                lastValue = cur_item[0]
                count = 1
            else:
                count += 1

            if cur_item[2] + 1 < len(arrs[cur_item[1]]):
                heappush(min_heap, (arrs[cur_item[1]][cur_item[2] + 1], cur_item[1], cur_item[2] + 1))

            if count == len(arrs):
                result += 1

        return result


if __name__ == '__main__':
    s = Solution3()
    print(s.intersectionOfArrays([[1, 2, 3], [3, 4, 5], [3, 9, 10]]))
    print(s.intersectionOfArrays([[1, 2, 3, 4], [1, 2, 5, 6, 7], [9, 10, 1, 5, 2, 3]]))
