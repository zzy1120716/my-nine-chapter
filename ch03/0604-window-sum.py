"""
604. 滑动窗口内数的和
给你一个大小为n的整型数组和一个大小为k的滑动窗口，
将滑动窗口从头移到尾，输出从开始到结束每一个时刻
滑动窗口内的数的和。

样例
对于数组 [1,2,7,8,5] ，滑动窗口大小k= 3 。
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
返回 [10,17,20]
"""
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if len(nums) < k or k <= 0:
            return []
        
        res = [0 for x in range(len(nums) - k + 1)]
        
        for i in range(k):
            res[0] += nums[i]
        
        for i in range(1, len(nums) - k + 1):
            res[i] = res[i - 1] - nums[i - 1] + nums[i + k - 1]
                
        return res