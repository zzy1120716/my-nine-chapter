"""
51. 上一个排列
给定一个整数数组来表示排列，找出其上一个排列。

样例
给出排列[1,3,2,3]，其上一个排列是[1,2,3,3]

给出排列[1,2,3,4]，其上一个排列是[4,3,2,1]

注意事项
排列中可能包含重复的整数
"""


# 思路同 #52
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        # 倒序遍历
        for i in range(len(nums) - 1, -1, -1):
            # 找到第一个数值变大的点，这样代表右边有小的可以和它换，而且可以保证是previous permutation
            if i > 0 and nums[i] < nums[i - 1]:
                # 找到后再次倒序遍历，找到第一个比刚才那个数值小的点，互相交换
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] < nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        # 因为之前保证了，右边这段数从右到左是一直变小的，所以直接双指针reverse
                        left, right = i, len(nums) - 1
                        while left <= right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        return nums
        # 如果循环结束了，表示没找到能替换的数，表示序列已经是最小的了
        nums.reverse()
        return nums


if __name__ == '__main__':
    ans = Solution().previousPermuation([1, 5, 8, 4, 7, 6, 5, 3, 1])
    print(ans)