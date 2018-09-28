"""
18. 子集 II
给定一个可能具有重复数字的列表，返回其所有可能的子集

样例
如果 S = [1,2,2]，一个可能的答案为：

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
挑战
你可以同时用递归与非递归的方式解决么？

注意事项
子集中的每个元素都是非降序的
两个子集间的顺序是无关紧要的
解集中不能包含重复子集
"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, startIndex, subset, results):
        results.append(subset[:])
        
        for i in range(startIndex, len(nums)):
            # 判断当前元素是否已在集合中
            if i != startIndex and nums[i] == nums[i - 1]:
                continue
            
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()