"""
80. 中位数
给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

样例
给出数组[4, 5, 1, 2, 3]， 返回 3

给出数组[7, 9, 4, 5]，返回 5

挑战
时间复杂度为O(n)
"""


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        return self.quick_select(nums, 0, len(nums) - 1, (len(nums) + 1) // 2)

    def quick_select(self, nums, start, end, size):
        mid = (start + end) // 2
        pivot = nums[mid]
        i, j = start - 1, end + 1
        k = start
        while k < j:
            if nums[k] < pivot:
                i += 1
                nums[i], nums[k] = nums[k], nums[i]
            elif nums[k] > pivot:
                j -= 1
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            k += 1
        if i - start + 1 >= size:
            return self.quick_select(nums, start, i, size)
        elif j - start >= size:
            return nums[j - 1]
        else:
            return self.quick_select(nums, j, end, size - (j - start))


if __name__ == '__main__':
    print(Solution().median([4, 5, 1, 2, 3]))

