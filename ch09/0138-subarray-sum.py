"""
138. 子数组之和
给定一个整数数组，找到和为零的子数组。你的代码应该返回满足
要求的子数组的起始位置和结束位置

样例
给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].

注意事项
There is at least one subarray that it's sum equals to zero.
"""


# 前缀和
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_hash = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i
            prefix_hash[prefix_sum] = i

        return -1, -1


class Solution1:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        result = []
        hash = {}
        hash[0] = -1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in hash:
                result.append(hash[sum] + 1)
                result.append(i)
                break
            hash[sum] = i
        return result


if __name__ == '__main__':
    print(Solution().subarraySum([-3, 1, 2, -3, 4]))
    print(Solution1().subarraySum([-3, 1, 2, -3, 4]))