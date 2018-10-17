"""
76. 最长上升子序列
给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

样例
给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3
给出 [4,2,4,5,3,7]，LIS 是 [2,4,5,7]，返回 4

挑战
要求时间复杂度为O(n^2) 或者 O(nlogn)

说明
最长上升子序列的定义：

最长上升子序列问题是在一个无序的给定序列中找到一个尽可能长的由低
到高排列的子序列，这种子序列不一定是连续的或者唯一的。
https://en.wikipedia.org/wiki/Longest_increasing_subsequence

https://segmentfault.com/a/1190000003819886
"""

"""
方法一：动态规划 O(n ^ 2)
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        # 存储每个位置的最长上升子序列长度
        lis = [0] * len(nums)
        max_len = 0
        for i in range(len(nums)):
            local_max = 0
            # 找出当前点之前的最大上升子序列长度
            for j in range(i):
                if lis[j] > local_max and nums[j] < nums[i]:
                    local_max = lis[j]
            # 当前点是该局部最大上升子序列长度加1
            lis[i] = local_max + 1
            # 用当前点的最大上升子序列长度更新全局最大长度
            max_len = max(max_len, lis[i])
        return max_len


"""
方法二：耐心排序法
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        # max_len表示当前最长升序序列的长度（为了方便操作tails我们减1）
        max_len = 0
        tails = [0] * len(nums)
        tails[0] = nums[0]
        # 根据三种情况更新不同升序序列的集合
        for i in range(1, len(nums)):
            if nums[i] < tails[0]:
                tails[0] = nums[i]
            elif nums[i] > tails[max_len]:
                max_len += 1
                tails[max_len] = nums[i]
            else:
                # 如果在中间，则二分搜索
                tails[self.binarySearch(tails, 0, max_len, nums[i])] = nums[i]
        return max_len + 1

    def binarySearch(self, tails, start, end, target):
        while start <= end:
            mid = start + (end - start) // 2
            if tails[mid] == target:
                return mid
            if tails[mid] < target:
                start = mid + 1
            if tails[mid] > target:
                end = mid - 1
        return start