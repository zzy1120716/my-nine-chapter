"""
15. 全排列
给定一个数字列表，返回其所有可能的排列。

样例
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
挑战
使用递归和非递归分别解决。

注意事项
你可以假设没有重复数字。
"""


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], results)
        return results
        
    def dfs(self, nums, visited, permutation, results):
        if len(nums) == len(permutation):
            results.append(permutation[:])
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, results)
            visited[i] = False
            permutation.pop()