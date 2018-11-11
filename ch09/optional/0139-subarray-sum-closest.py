"""
139. 最接近零的子数组和
给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最右一个指数。
你的代码应该返回满足要求的子数组的起始位置和结束位置

样例
给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]。

挑战
O(nlogn)的时间复杂度
"""


# 方法一：HashMap + Array + Sort 的方法。用 HashMap 记录之前的位置，用 Array 来打擂台找最小差距
# 时间复杂度为O(nlogn), 空间复杂度为O(n)
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        results = [0] * 2

        # edge case
        if not nums:
            return []
        if len(nums) == 1:
            return [0, 0]

        # general
        h = {0: -1}
        prefix_sum = [0] * (len(nums) + 1)
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum in h:
                results[0] = h[curr_sum] + 1
                results[1] = i
                return results
            h[curr_sum] = i
            prefix_sum[i + 1] = curr_sum

        prefix_sum.sort()

        min_diff = float('inf')
        left = right = 0

        for i in range(len(prefix_sum) - 1):
            if min_diff > abs(prefix_sum[i] - prefix_sum[i + 1]):
                min_diff = abs(prefix_sum[i] - prefix_sum[i + 1])
                left = prefix_sum[i]
                right = prefix_sum[i + 1]

        if h[left] < h[right]:
            results[0] = h[left] + 1
            results[1] = h[right]
        else:
            results[0] = h[right] + 1
            results[1] = h[left]

        return results


# 方法二：官方答案，tuple list
class Solution1:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        prefix_sum = [(0, -1)]
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))

        prefix_sum.sort()

        closest, answer = float('inf'), []
        for i in range(1, len(prefix_sum)):
            if closest > prefix_sum[i][0] - prefix_sum[i - 1][0]:
                closest = prefix_sum[i][0] - prefix_sum[i - 1][0]
                left = min(prefix_sum[i - 1][1], prefix_sum[i][1]) + 1
                right = max(prefix_sum[i - 1][1], prefix_sum[i][1])
                answer = [left, right]

        return answer


# 方法三：创建class Pair存储前缀和
from functools import total_ordering


@total_ordering
class Pair:
    def __init__(self, s, i):
        self.sum = s
        self.index = i

    def __lt__(self, other):
        return self.sum < other.sum

    def __eq__(self, other):
        return self.sum == other.sum


class Solution2:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        res = [0] * 2
        if not nums:
            return res

        if len(nums) == 1:
            res[0] = res[1] = 0
            return res

        sums = [None] * (len(nums) + 1)
        prev = 0
        sums[0] = Pair(0, 0)
        for i in range(1, len(nums) + 1):
            sums[i] = Pair(prev + nums[i - 1], i)
            prev = sums[i].sum

        sums.sort()
        ans = float('inf')
        for i in range(1, len(nums) + 1):
            if ans > sums[i].sum - sums[i - 1].sum:
                ans = sums[i].sum - sums[i - 1].sum
                tmp = [sums[i].index - 1, sums[i - 1].index - 1]
                tmp.sort()
                res[0] = tmp[0] + 1
                res[1] = tmp[1]

        return res


# 方法四：使用堆
from heapq import heappush, heappop
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, v, i):
        self.val = v
        self.index = i

    def __lt__(self, other):
        if self.val == other.val:
            return self.index < other.index
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val and self.index == other.index


class Solution3:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        q = [Node(0, -1)]
        sum = start = end = 0
        ans = [0] * 2
        for i in range(len(nums)):
            sum += nums[i]
            heappush(q, Node(sum, i))

        pre = heappop(q)
        min_val = float('inf')
        while q:
            curr = heappop(q)
            if min_val > abs(curr.val - pre.val):
                min_val = abs(curr.val - pre.val)
                ans[0] = min(pre.index, curr.index) + 1
                ans[1] = max(pre.index, curr.index)
            pre = curr

        return ans


if __name__ == '__main__':
    print(Solution3().subarraySumClosest([-3, 1, 1, -3, 5]))