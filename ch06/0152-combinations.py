"""
152. 组合
Given two integers n and k, return all possible 
combinations of k numbers out of 1 ... n.

样例
Given n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]
]
注意事项
You don't need to care the order of combinations, 
but you should make sure the numbers in a combination 
are sorted.
"""
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp, results)
        return results
    
    def dfs(self, n, k, m, p, tmp, results):
        if k == p:
            results.append(tmp[:])
            return
        for i in range(m, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, p + 1, tmp, results)
            tmp.pop()