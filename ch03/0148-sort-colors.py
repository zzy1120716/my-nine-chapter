"""
148. 颜色分类
给定一个包含红，白，蓝且长度为 n 的数组，将数组
元素进行分类使相同颜色的元素相邻，并按照红、白、蓝
的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

样例
给你数组 [1, 0, 1, 2], 需要将该数组原地排序为
[0, 1, 1, 2]。

挑战
一个相当直接的解决方案是使用计数排序扫描2遍的算法。

首先，迭代数组计算 0,1,2 出现的次数，然后依次用
0,1,2 出现的次数去覆盖数组。

你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历
一遍数组的算法？

注意事项
不能使用代码库中的排序函数来解决这个问题。
排序需要在原数组中进行。
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return
        
        left, right, i = 0, len(nums) - 1, 0
        
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1