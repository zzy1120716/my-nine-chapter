"""
521. 去除重复元素
给一个整数数组，去除重复的元素。

你应该做这些事

1.在原数组上操作
2.将去除重复之后的元素放在数组的开头
3.返回去除重复元素之后的元素个数

样例
给出 nums = [1,3,1,4,4,2],你需要做以下操作

1.将重复元素扔在最后面 => nums = [1,3,4,2,?,?].
2.返回个数 4
实际上我们并不在意?是什么

挑战
1.O(n)时间复杂度.
2.O(nlogn)时间复杂度但没有额外空间

注意事项
不需要保持原数组的顺序
"""


# 方法一：Hash，O(n) time，O(n) space
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1
        return result


# 方法二：排序，O(nlogn) time，O(1) space
class Solution1:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        result = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        return result


# 方法三：类似方法二，但使用双指针
class Solution2:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        if len(nums) == 0:
            return 1

        left, right = 0, 1
        nums.sort()

        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1


# 方法一改进：使用set代替dict
class Solution3:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        unique = set()
        left = right = 0

        while right < len(nums):
            if nums[right] not in unique:
                nums[left], nums[right] = nums[right], nums[left]
                unique.add(nums[left])
                left += 1
            right += 1

        return left


if __name__ == '__main__':
    nums = [1, 3, 1, 4, 4, 2]
    print(Solution3().deduplication(nums))
    print(nums)
