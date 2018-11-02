"""
652. 因式分解
一个非负数可以被视为其因数的乘积。编写一个函数来返回整数 n 的因数所有可能组合。

样例
给出 n = 8
返回 [[2,2,2],[2,4]]
// 8 = 2 x 2 x 2 = 2 x 4

给出 n = 1
返回 []

给出 n = 1
返回 [[2,6],[2,2,3],[3,4]]

注意事项
组合中的元素(a1,a2,...,ak)必须是非降序。(即，a1≤a2≤...≤ak)。
结果集中不能包含重复的组合。
"""

# 传统的DFS模板
import math


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        result = []
        self.dfs(n, 2, [], result)
        return result

    def dfs(self, n, last_factor, path, result):
        if path:
            path.append(n)
            result.append(path[:])
            path.pop()
        for i in range(last_factor, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue
            path.append(i)
            self.dfs(n // i, i, path, result)
            # backtracking
            path.pop()


class Solution1:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = []
        self.dfs(n, 2, [], results)
        return results

    def dfs(self, n, start, subset, results):
        if n <= 1:
            if len(subset) > 1:
                results.append(subset[:])
            return

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                subset.append(i)
                self.dfs(n // i, i, subset, results)
                subset.pop()

        if n >= start:
            subset.append(n)
            self.dfs(1, n, subset, results)
            subset.pop()


class Solution2:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = []
        self.helper(n, [], results)
        return results

    def helper(self, n, path, results):
        if not path:
            pre = 2
        else:
            pre = path[-1]
        for i in range(pre, int(math.sqrt(n)) + 1):
            if n % i == 0:
                path.append(i)
                so = path[:]
                so.append(n // i)
                results.append(so)
                self.helper(n // i, path, results)
                path.pop()


if __name__ == '__main__':
    s = Solution2()
    result = s.getFactors(12)
    print(result)