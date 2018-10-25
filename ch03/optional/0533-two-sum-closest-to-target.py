"""
533. 两数和的最接近值
找到两个数字使得他们和最接近target

样例
nums = [-1, 2, 1, -4],target = 4.

最接近值为 1

挑战
Do it in O(nlogn) time complexity.
"""

"""
双指针：
从左右不断向target逼近
由于只求最接近的和与target之差，
所以用变量保存当前最小值，打擂台即可
"""
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1

        diff = sys.maxsize
        while left < right:
            if nums[left] + nums[right] < target:
                diff = min(diff, target - nums[left] - nums[right])
                left += 1
            else:
                diff = min(diff, nums[left] + nums[right] - target)
                right -= 1

        return diff