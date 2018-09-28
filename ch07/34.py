"""
34. N皇后问题 II
根据n皇后问题，现在返回n皇后不同的
解决方案的数量而不是具体的放置布局。

样例
比如n=4，存在2种解决方案
"""
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.result = 0
        visited = {
            'col': set(),
            'sum': set(),
            'diff': set()
        }
        self.dfs(n, [], visited)
        return self.result
        
    def dfs(self, n, permutation, visited):
        if n == len(permutation):
            self.result += 1
            return
        
        row = len(permutation)
        for col in range(n):
            if not self.is_valid(permutation, visited, col):
                continue
            permutation.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            self.dfs(n, permutation, visited)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            permutation.pop()
            
    def is_valid(self, permutation, visited, col):
        row = len(permutation)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True