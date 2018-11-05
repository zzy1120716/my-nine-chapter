"""
17. 子集
给定一个含不同整数的集合，返回其所有的子集

样例
如果 S = [1,2,3]，有如下的解：

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
挑战
你可以同时用递归与非递归的方式解决么？

注意事项
子集中的元素排列必须是非降序的，解集必须不包含重复的子集
"""
# 最简单的0/1递归方式
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    # 1、递归的定义
    def dfs(self, nums, index, subset, results):
        
        # 3、递归的出口
        if index == len(nums):
            results.append(subset[:])
            return
        
        # 2、递归的拆解
        # 选 nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, results)
        
        # 不选 nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, results)

# 可以扩展到排列类搜索的递归方式
class Solution1:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        return results
    
    def dfs(self, nums, startIndex, subset, results):
        results.append(subset[:])   # deep copy
        
        for i in range(startIndex, len(nums)):
            # [1] => [1,2]
            # 去寻找以[1,2]开头的所有子集
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            # [1,2] => [1]
            subset.pop()    # backtracking

# 每次传递一个新的list，省略backtracking的步骤
class Solution2:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, startIndex, subset, results):
        
        results.append(subset)
        
        for i in range(startIndex, len(nums)):
            newSet = subset[:]
            newSet.append(nums[i])
            self.dfs(nums, i + 1, newSet, results)


if __name__ == '__main__':
    ans = Solution().subsets([1, 2, 3])
    print(ans)