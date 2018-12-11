"""
48. 主元素 III
给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的1/k。

样例
给出数组 [3,1,2,3,2,3,3,4,4,4] ，和 k = 3，返回 3

挑战
要求时间复杂度为O(n)，空间复杂度为O(k)

注意事项
数组中只有唯一的主元素
"""
import collections
import sys


# 方法一：Hash
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        for num, cnt in d.items():
            if cnt > len(nums) // k:
                return num
        return


# 方法二：Boyer-Moore Majority Vote algorithm
class Solution1:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        candidate = [-sys.maxsize] * (k - 1)
        frequency = [0] * (k - 1)

        for i in range(len(nums)):
            found = False
            available = -sys.maxsize
            for j in range(k - 1):
                if nums[i] == candidate[j]:
                    frequency[j] += 1
                    found = True
                    break
                if frequency[j] <= 0:
                    available = j
                    frequency[j] = 0
                    candidate[j] = -sys.maxsize
            if not found:
                if available >= 0:
                    candidate[available] = nums[i]
                    frequency[available] = 1
                else:
                    for j in range(k - 1):
                        frequency[j] -= 1

        max_frequency = 0
        max_frequency_num = -sys.maxsize
        for i in range(k - 1):
            frequency[i] = 0
            for j in range(len(nums)):
                if nums[j] == candidate[i]:
                    frequency[i] += 1
                    if frequency[i] > max_frequency:
                        max_frequency = frequency[i]
                        max_frequency_num = candidate[i]

        return max_frequency_num


if __name__ == '__main__':
    print(Solution1().majorityNumber([3, 1, 2, 3, 2, 3, 3, 4, 4, 4], 3))
