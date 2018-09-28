"""
135. 数字组合
给出一个候选数字的set(C)和目标数字(T),找到C中所有的组合，
使找出的数字和为T。C中的数字可以无限制重复被选取。

例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：

[7]，

[2,2,3]

样例
给出候选set[2,3,6,7]和目标数字7

返回 [[7],[2,2,3]]

注意事项
所有的数字(包括目标数字)均为正整数。
元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
解集不能包含重复的组合。 
"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(list(set(candidates))) # 去重并排序
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
    
    def dfs(self, candidates, target, start, combination, results):
        if target == 0:
            # deep copy
            return results.append(list(combination))
        
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            
            # [2] => [2, 2]
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2, 2] => [2]
            combination.pop()   # backtracking