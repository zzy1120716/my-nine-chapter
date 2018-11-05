"""
52. 下一个排列
给定一个整数数组来表示排列，找出其之后的一个排列。

样例
给出排列[1,3,2,3]，其下一个排列是[1,3,3,2]

给出排列[4,3,2,1]，其下一个排列是[1,2,3,4]

注意事项
排列中可能包含重复的整数
"""

"""
1. 从后往前找到第一个比前一个小的元素的下标i
2. 从后往前找一个刚刚比下标i对应元素大的元素，从len(nums) - 1到i + 1，下标为j
3. 交换下标i和j的两个元素
4. 将从i + 1到len(nums) - 1的元素逆序
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1, len(nums) - 1)
        return nums

    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# for循环版本
class Solution1:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        # 倒序遍历
        for i in range(len(nums) - 1, -1, -1):
            # 找到第一个数值变小的点，这样代表右边有大的可以和它换，而且可以保证是next permutation
            if i > 0 and nums[i] > nums[i - 1]:
                # 找到后再次倒序遍历，找到第一个比刚才那个数值大的点，互相交换
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        # 因为之前保证了，右边这段数从右到左是一直变大的，所以直接双指针reverse
                        left, right = i, len(nums) - 1
                        while left <= right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        return nums
        # 如果循环结束了，表示没找到能替换的数，表示序列已经是最大的了
        nums.reverse()
        return nums


if __name__ == '__main__':
    ans = Solution().nextPermutation([1, 5, 8, 4, 7, 6, 5, 3, 1])
    print(ans)