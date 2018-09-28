"""
552. 创建最大数
给出两个长度分别是m和n的数组来表示两个大整数，数组的
每个元素都是数字0-9。从这两个数组当中选出k个数字来创
建一个最大数，其中k满足k <= m + n。选出来的数字在创建
的最大数里面的位置必须和在原数组内的相对位置一致。返回
k个数的数组。你应该尽可能的去优化算法的时间复杂度和空
间复杂度。

样例
给出 nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
返回 [9, 8, 6, 5, 3]

给出 nums1 = [6, 7], nums2 = [6, 0, 4], k = 5
返回 [6, 7, 6, 0, 4]

给出 nums1 = [3, 9], nums2 = [8, 9], k = 3
返回 [9, 8, 9]
"""
class Solution:
    """
    @param nums1: an integer array of length m with digits 0-9
    @param nums2: an integer array of length n with digits 0-9
    @param k: an integer and k <= m + n
    @return: an integer array
    """
    def maxNumber(self, nums1, nums2, k):
        # write your code here
        len1, len2 = len(nums1), len(nums2)
        res = []
        # nums1 = [3, 4, 6, 5]
        # nums2 = [9, 1, 2, 5, 8, 3]
        # k = 5
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = self.merge(self.getMax(nums1, x), self.getMax(nums2, k - x))
            res = max(tmp, res)
        return res
        
    """
    找出数组中前t大的数
    例如：getMax([9, 1, 2, 5, 8, 3], 5)
    输出[9, 2, 5, 8, 3]
    @param nums: 输入数组
    @param t: 输出数组的长度
    @return: 前t大的数组成的数组，顺序不变
    """
    def getMax(self, nums, t):
        ans = []
        size = len(nums)
        for x in range(size):
            while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                ans.pop()
            if len(ans) < t:
                ans.append(nums[x])
        return ans
    
    """
    拼接两个数组
    例如：
    merge([3, 4, 6, 5], [9, 1, 2, 5, 8, 3])
    输出[9, 3, 4, 6, 5, 1, 2, 5, 8, 3]
    merge([3, 4], [5, 6])
    输出[5, 6, 3, 4]
    @param nums1: 输入数组1
    @param nums2: 输入数组2
    @return: 两个数组的和，数字最大
    """
    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]