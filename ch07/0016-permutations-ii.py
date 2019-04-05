"""
16. 带重复元素的排列
给出一个具有重复数字的列表，找出列表所有不同的排列。

样例
给出列表 [1,2,2]，不同的排列有：

[
  [1,2,2],
  [2,1,2],
  [2,2,1]
]
挑战
使用递归和非递归分别完成该题。
"""


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        # write your code here
        results = []
        visited = [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], results)
        return results

    def dfs(self, nums, visited, permutation, results):
        if len(nums) == len(permutation):
            results.append(permutation[:])
            return
        
        for i in range(len(nums)):
            # 此处增加判断条件
            if visited[i] or (visited[i - 1] and i > 0 and nums[i] == nums[i - 1]):
                continue
            
            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, results)
            visited[i] = False
            permutation.pop()