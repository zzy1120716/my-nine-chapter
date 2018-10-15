"""
603. 最大整除子集
给一个由 无重复的正整数 组成的集合，找出满足任意两个元素
(Si, Sj) 都有 Si % Sj = 0 或 Sj % Si = 0 成立的最大子集

样例
给一个数组 [1,2,3]，返回 [1,2] 或 [1,3]
给一个数组 [1,2,4,8]，返回 [1,2,4,8]

注意事项
如果有多种解集，返回其中任意一个。
"""
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        n = len(nums)
        # 记录最大整除数组的长度
        dp = [1] * n
        # 记录到当前元素最大size的前一位数的index
        parent = [-1] * n

        nums.sort()
        m, index = 0, -1

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] >= m:
                m = dp[i]
                index = i

        result = []
        for i in range(m):
            result.append(nums[index])
            index = parent[index]

        return result