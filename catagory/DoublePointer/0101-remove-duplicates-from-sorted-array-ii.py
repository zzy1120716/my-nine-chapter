"""
101. 删除排序数组中的重复数字 II
跟进“删除重复数字”：

如果可以允许出现两次重复将如何处理？

样例
给出数组A =[1,1,1,2,2,3]，你的函数应该返回长度5，此时A=[1,1,2,2,3]。
"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        tmp = None
        count = 1
        for i in range(len(nums), 0, -1):
            if tmp == nums[i - 1]:
                if count < 2:
                    count += 1
                else:
                    nums.pop(i - 1)
            else:
                tmp = nums[i - 1]
                count = 1
        return len(nums)


# 第一种，最简练，借助于一个巧妙的观察：虽然不能和 left 比较来直接判定重复
# 的数是否要并入（因为可允许一个重复的数），但可以和 left 前两个比。
class Solution1:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n < 3:
            return n

        left = 2
        for right in range(2, n):
            if nums[left - 2] != nums[right]:
                nums[left] = nums[right]
                left += 1

        return left


# 第二种，最常见的解法，第一次看见这题最可能想到的解法。特点是，
# 读指针 right 一直匀速往前，写入指针 left 有时遇到重复的数会停一下。
class Solution2:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n < 3:
            return n

        left = 0
        count = 1
        for right in range(1, n):
            if nums[left] == nums[right]:
                count += 1
            else:
                count = 1

            if count <= 2:
                left += 1
                nums[left] = nums[right]

        return left + 1


# 第三种，从没在别处见过，和第二种相对，写入指针 left 一直匀速往前，
# 读指针 right 有时遇到重复的数会跳跃前进。
class Solution3:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n < 3:
            return n

        left, right = 0, 1
        while right < n:
            repeated = False
            while right < n and nums[right] == nums[left]:
                right += 1
                repeated = True

            if not repeated:
                right += 1

            left += 1
            nums[left] = nums[right - 1]

        return left + 1


if __name__ == '__main__':
    print(Solution2().removeDuplicates([1, 1, 1, 2, 2, 3]))
