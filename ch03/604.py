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