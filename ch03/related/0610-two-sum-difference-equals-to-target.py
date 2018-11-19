"""
610. 两数和 - 差等于目标值
给定一个整数数组，找到两个数的 差 等于目标值。
index1必须小于index2。注意返回的index1和index2
不是 0-based。

样例
给定的数组为 [2,7,15,24]，目标值为 5，返回 [1,2] (7 - 2 = 5)

注意事项
保证只有一个答案。
"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        n, indexs = len(nums), []
        nums = sorted(nums, key=lambda x: x[0])
        
        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                indexs = [nums[i][1] + 1, nums[j][1] + 1]
        
        if indexs[0] > indexs[1]:
            indexs[0], indexs[1] = indexs[1], indexs[0]
            
        return indexs