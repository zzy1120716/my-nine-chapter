"""
153. 数字组合 II
给出一组候选数字(C)和目标数字(T),找出C中所有的组合，使组合中
数字的和为T。C中每个数字在每个组合中只能使用一次。

样例
给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,

解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]

注意事项
所有的数字(包括目标数字)均为正整数。
元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
解集不能包含重复的组合。
"""
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        results, tmp, use = [], [], [0] * len(num)
        self.dfs(num, target, 0, 0, tmp, use, results)
        return results
        
    def dfs(self, num, target, p, now, tmp, use, results):
        if now == target:
            results.append(tmp[:])
            return
        for i in range(p, len(num)):
            if now + num[i] <= target and (i == 0 or num[i] != num[i - 1] or use[i - 1] == 1):
                tmp.append(num[i])
                use[i] = 1
                self.dfs(num, target, i + 1, now + num[i], tmp, use, results)
                tmp.pop()
                use[i] = 0