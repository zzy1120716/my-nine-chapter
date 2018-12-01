"""
191. 乘积最大子序列
找出一个序列中乘积最大的连续子序列（至少包含一个数）。

样例
比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。
"""


# LeetCode
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        n = len(nums)
        max_prod = [nums[0]] + [0] * (n - 1)
        min_prod = [nums[0]] + [0] * (n - 1)

        result = nums[0]
        for i in range(1, n):
            min_prod[i] = max_prod[i] = nums[i]
            if nums[i] > 0:
                max_prod[i] = max(max_prod[i], max_prod[i - 1] * nums[i])
                min_prod[i] = min(min_prod[i], min_prod[i - 1] * nums[i])
            elif nums[i] < 0:
                max_prod[i] = max(max_prod[i], min_prod[i - 1] * nums[i])
                min_prod[i] = min(min_prod[i], max_prod[i - 1] * nums[i])

            result = max(result, max_prod[i])

        return result


# O(1) Space Complexity
class Solution1:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        max_pre = min_pre = nums[0]
        # max_prod = min_prod = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            max_prod = max(nums[i], max(max_pre * nums[i], min_pre * nums[i]))
            min_prod = min(nums[i], min(max_pre * nums[i], min_pre * nums[i]))
            result = max(result, max_prod)
            max_pre = max_prod
            min_pre = min_prod
        return result


if __name__ == '__main__':
    print(Solution1().maxProduct([2, 3, -2, 4]))
