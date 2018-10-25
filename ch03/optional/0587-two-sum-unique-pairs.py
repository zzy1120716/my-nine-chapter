"""
587. 两数之和 - 不同组成
给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值,
返回对数.

样例
给一数组 nums = [1,1,2,45,46,46], target = 47, 返回 2
1 + 46 = 47
2 + 45 = 47
"""

"""
方法一：hash，value记录是否已使用过，1代表已用，0代表未用
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        hash = {}
        count = 0
        for i in range(len(nums)):
            if target - nums[i] in hash and hash[target - nums[i]] == 0:
                count += 1
                hash[target - nums[i]] = 1
                hash[nums[i]] = 1
            if nums[i] not in hash:
                hash[nums[i]] = 0
        return count


"""
方法二：双指针，遇到满足的数对不退出循环，接着找，注意去重
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                count, left, right = count + 1, left + 1, right - 1
                # 遇到与前（后）一个数相同，需要向后（前）移动一位
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return count