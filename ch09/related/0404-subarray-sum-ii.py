"""
404. 子数组求和 II
给定一个正整数数组及一个区间，找到一个子数组，使得其数字的总和在给定区间范围内。请返回所有可能答案的数量。

样例
给定数组[1,2,3,4] 及 区间 = [1,3]， 返回 4。 所有可能的答案如下：

[0, 0]
[0, 1]
[1, 1]
[2, 2]
"""


# 相关题 #138 subarray-sum

# 方法一：同向双指针模板
# 时间复杂度 O(N)
# 这个题的双指针是一个加强版，以前的题，右边的指针只需要一个。
# 这个题因为需要知道 < start 和 <= end 的两个位置。因此需要多一个指针。
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        big_sum, small_sum = 0, 0
        big_end, small_end = 0, 0
        ans = 0
        for i in range(n):
            small_end = max(small_end, i)
            big_end = max(big_end, i)
            while small_end < n and small_sum + A[small_end] < start:
                small_sum += A[small_end]
                small_end += 1
            while big_end < n and big_sum + A[big_end] <= end:
                big_sum += A[big_end]
                big_end += 1

            if big_end - small_end > 0:
                ans += big_end - small_end

            if small_end > i:
                small_sum -= A[i]

            if big_end > i:
                big_sum -= A[i]

        return ans


# 方法二：二分法
class Solution1:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        size = len(A)
        sums = [0] * (size + 1)
        for i in range(size):
            sums[i] = sums[i - 1] + A[i]

        result = 0
        for i in range(size):
            # bisect left
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] < start:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == size: break
            left = lo

            # bisect right
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] > end:
                    hi = mid
                else:
                    lo = mid + 1
            if lo == i and A[i] > size:
                continue
            right = lo

            result += right - left

        return result