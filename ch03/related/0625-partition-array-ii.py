"""
625. 数组划分II
将一个没有经过排序的整数数组划分为 3 部分:
1.第一部分中所有的值都 < low
2.第二部分中所有的值都 >= low并且 <= high
3.第三部分中所有的值都 > high
返回任意一种可能的情况。

样例
给出数组 [4,3,4,1,2,3,1,2] ，low = 2，high = 3。
变为 [1,1,2,3,2,3,4,4]
([1,1,2,2,3,3,4,4] 也是正确答案，但 [1,2,1,2,3,3,4,4] 不是)

挑战
1.在原地完成
2.用一个循环完成

注意事项
在所有测试数组中都有 low <= high。
"""


# 方法一：三指针
class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        if len(nums) <= 1:
            return

        pl, pr = 0, len(nums) - 1
        i = 0
        while i <= pr:
            if nums[i] < low:
                nums[pl], nums[i] = nums[i], nums[pl]
                pl += 1
                i += 1
            elif nums[i] > high:
                nums[pr], nums[i] = nums[i], nums[pr]
                pr -= 1
            else:
                i += 1


# 方法二：两次划分
class Solution1:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        left, right = 0, len(nums) - 1
        # 首先把两个区间分为 < low 和 >= low 的两个部分
        while left <= right:
            while left <= right and nums[left] < low:
                left += 1
            while left <= right and nums[right] >= low:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        right = len(nums) - 1
        # 然后从 >= low 的部分里分出 <= high 和 > high 的两个部分
        while left <= right:
            while left <= right and nums[left] <= high:
                left += 1
            while left <= right and nums[right] > high:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


if __name__ == '__main__':
    nums = [4, 3, 4, 1, 2, 3, 1, 2]
    Solution1().partition2(nums, 2, 3)
    print(nums)
