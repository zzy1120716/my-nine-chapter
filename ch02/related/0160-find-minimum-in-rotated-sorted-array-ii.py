"""
160. 寻找旋转排序数组中的最小值 II
假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

数组中可能存在重复的元素。

样例
给出[4,4,5,6,7,0,1,2]  返回 0

注意事项
The array may contain duplicates.
"""


# 这道题目在面试中不会让写完整的程序
# 只需要知道最坏情况下[1, 1, 1...., 1]里有一个0
# 这种情况使得时间复杂度必须是O(n)
# 因此写一个for循环就好了。
# 如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
# 反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == nums[end]:
                # if mid equals to end, that means it's fine to remove end
                # the smallest element won't be removed
                end -= 1
            elif nums[mid] < nums[end]:
                # == & < can be merged
                end = mid
            else:
                # or start = mid + 1
                start = mid

        if nums[start] <= nums[end]:
            return nums[start]
        return nums[end]