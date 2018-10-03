"""
547. 两数组的交集
给出两个数组，写出一个方法求出它们的交集

样例
nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

挑战
可以用三种不同的方法实现吗？

注意事项
Each element in the result must be unique.
The result can be in any order.
"""

"""
方法一：python build-in set operation
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        # return list(set(nums1).intersection(nums2))
        return list(set(nums1) & set(nums2))

"""
方法二：hash set
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        result = []
        nums1_uni = set(nums1)
        for num in nums2:
            if num in nums1_uni:
                result.append(num)
                nums1_uni.discard(num)
        return result

"""
方法三：binary search + hash set
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1
        else:
            s_nums = nums1
            b_nums = nums2

        s_nums.sort()
        for num in b_nums:
            if self.binary_search(s_nums, num):
                result.add(num)
        return list(result)

    def binary_search(self, nums, target):
        if not nums or len(nums) == 0:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] <= target:
                start = mid
            elif nums[mid] > target:
                end = mid

        if nums[end] == target or nums[start] == target:
            return True
        return False

"""
方法四：sort + two pointers
"""
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        result = []

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    i += 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    j += 1

            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return result