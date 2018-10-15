"""
513. 完美平方
给一个正整数 n, 找到若干个完全平方数(比如1, 4, 9, ... )
使得他们的和等于 n。你需要让平方数的个数最少。

样例
给出 n = 12, 返回 3 因为 12 = 4 + 4 + 4。
给出 n = 13, 返回 2 因为 13 = 4 + 9。
"""

"""
方法一：动态规划
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # cntPerfectSquares[i] = 和为i的完美平方数的最小数量
        # 注意：cntPerfectSquares[0]是0
        cntPerfectSquares = [sys.maxsize] * (n + 1)
        cntPerfectSquares[0] = 0

        for i in range(1, n + 1):
            j = 1
            # 对每个i，都是(i - j * j)与一个完美平方数(j * j)的和
            while j * j <= i:
                cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j * j] + 1)
                j += 1

        return cntPerfectSquares[-1]


"""
方法二：静态动态规划
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # cntPerfectSquares[i] = 和为i的完美平方数的最小数量
        # 因为cntPerfectSquares是静态list，如果len(cntPerfectSquares) > n
        # 那么在上一次函数调用之后，我们已经计算出结果，
        # 并且我们现在就可以返回结果
        cntPerfectSquares = [0]

        # 当len(cntPerfectSquares) <= n时，我们需要增量计算
        # 下一个结果直到得到n的结果
        while len(cntPerfectSquares) <= n:
            m = len(cntPerfectSquares)
            cntSquares = sys.maxsize
            i = 1
            while i * i <= m:
                cntSquares = min(cntSquares, cntPerfectSquares[m - i * i] + 1)
                i += 1

            cntPerfectSquares.append(cntSquares)

        return cntPerfectSquares[-1]


"""
方法三：数学方法（四平方和定理）
每个正整数均可表示为4个整数的平方和
结果只能为1,2,3,4中的一个
"""
class Solution:
    """
    @param n: a positive integer
    @return: True or False
    """
    def is_square(self, n):
        sqrt_n = int(math.sqrt(n))
        return sqrt_n * sqrt_n == n

    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # n是完美平方数，返回1
        if self.is_square(n):
            return 1

        # 如果n能够写成 4 ^ k * (8 * m + 7) 的形式
        # 则返回4，参见Legendre's three-square theorem
        while n & 3 == 0:  # n % 4 == 0
            n >>= 2

        if n & 7 == 7:  # n % 8 == 7
            return 4

        # 检查是否应返回2
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if self.is_square(n - i * i):
                return 2

        # 均不满足，则返回3
        return 3


"""
方法四：BFS
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # perfectSquares包含所有小于等于n的完美平方数
        perfectSquares = []
        # cntPerfectSquares[i - 1] = 和为i的完美平方数的最小数量
        cntPerfectSquares = [0] * n

        # 获取所有小于等于n的完美平方数
        i = 1
        while i * i <= n:
            perfectSquares.append(i * i)
            cntPerfectSquares[i * i - 1] = 1
            i += 1

        # 如果n是完美平方数，则立即返回1
        if perfectSquares[-1] == n:
            return 1

        # 考虑一个由数字0,1，...，n组成的图形作为其节点。
        # 当且仅当j = i +（完美平方数）或i = j +（完美平方数）时，
        # 节点j通过边连接到节点i。 从节点0开始，进行广度优先搜索。
        # 如果我们在步骤m到达节点n，那么总和为n的最小数量的完全平方数是m。
        # 在这里，由于我们已经获得了完美的平方数，我们实际上已经完成了第1步的搜索。
        queue = collections.deque([])
        for i in perfectSquares:
            queue.append(i)

        currCntPerfectSquares = 1
        while queue:
            currCntPerfectSquares += 1

            size = len(queue)
            for i in range(size):
                tmp = queue[0]
                # 检查节点tmp的邻居，它们是tmp和完美平方数的和。
                for j in perfectSquares:
                    if tmp + j == n:
                        # 到达了节点n
                        return currCntPerfectSquares
                    elif tmp + j < n and cntPerfectSquares[tmp + j - 1] == 0:
                        # 如果cntPerfectSquares[tmp + j - 1]> 0，
                        # 这不是我们第一次访问此节点，我们应该跳过节点(tmp + j)。
                        cntPerfectSquares[tmp + j - 1] = currCntPerfectSquares
                        queue.append(tmp + j)
                    # 不需要考虑大于n的节点
                    elif tmp + j > n:
                        break

                queue.popleft()

        return 0


"""
方法五：DFS 记忆化搜索
使用dfs，先找到所有小于target的平方数，循环选取各数
用target减去向下递归。map用来记录分割当前target所需要
的least number
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        candidates = []
        num = 1
        while num * num <= n:
            candidates.append(num * num)
            num += 1
        result = self.dfs(n, candidates, {})
        return result

    def dfs(self, target, candidates, memo):
        if target in memo:
            return memo[target]
        least = sys.maxsize
        if target == 0:
            return 0
        for i in range(len(candidates) - 1, -1, -1):
            if target - candidates[i] < 0:
                continue
            nxt = self.dfs(target - candidates[i], candidates, memo)
            least = min(least, nxt + 1)
        memo[target] = least
        return least