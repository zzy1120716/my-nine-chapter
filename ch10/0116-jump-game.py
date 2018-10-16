"""
116. 跳跃游戏
给出一个非负整数数组，你最初定位在数组的第一个位置。　　　
数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　
判断你是否能到达数组的最后一个位置。

样例
A = [2,3,1,1,4]，返回 true.
A = [3,2,1,0,4]，返回 false.

注意事项
这个问题有两个方法，一个是贪心和 动态规划。
贪心方法时间复杂度为O（N）。
动态规划方法的时间复杂度为为O（n^2）。
我们手动设置小型数据集，使大家可以通过测试的两种方式。
这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。
如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。
"""
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        dp = [1] + [0] * (n - 1)
        for i in range(n):
            if dp[i] == 0:
                continue
            for j in range(A[i]):
                if i + j + 1 < n:
                    dp[i + j + 1] = 1
        return dp[-1] == 1


"""
方法一：回溯法
"""
class Solution:
    """
    @param A: A integer
    @param A: A list of integers
    @return: A boolean
    """
    def canJumpFromPosition(self, position, A):
        if position == len(A) - 1:
            return True

        furthestJump = min(position + A[position], len(A) - 1)
        # old
        # for nextPosition in range(position + 1, furthestJump + 1):
        # new
        for nextPosition in range(furthestJump, position, -1):
            if self.canJumpFromPosition(nextPosition, A):
                return True

        return False

    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        return self.canJumpFromPosition(0, A)


"""
方法二：自顶向下动态规划
"""
from enum import Enum
Index = Enum('Index', ('GOOD', 'BAD', 'UNKNOWN'))

class Solution:

    memo = []

    """
    @param A: A integer
    @param A: A list of integers
    @return: A boolean
    """
    def canJumpFromPosition(self, position, A):
        if self.memo[position] != Index.UNKNOWN:
            return True if self.memo[position] == Index.GOOD else False

        furthestJump = min(position + A[position], len(A) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, A):
                self.memo[position] = Index.GOOD
                return True

        self.memo[position] = Index.BAD
        return False

    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        self.memo = [Index.UNKNOWN] * len(A)
        self.memo[len(self.memo) - 1] = Index.GOOD
        return self.canJumpFromPosition(0, A)


"""
方法三：自底向上动态规划
"""
from enum import Enum
Index = Enum('Index', ('GOOD', 'BAD', 'UNKNOWN'))

class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        memo = [Index.UNKNOWN] * len(A)
        memo[len(memo) - 1] = Index.GOOD

        for i in range(len(A) - 2, -1, -1):
            furthestJump = min(i + A[i], len(A) - 1)
            for j in range(i + 1, furthestJump + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break

        return memo[0] == Index.GOOD


"""
方法四：贪心法
"""
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        lastPos = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if i + A[i] >= lastPos:
                lastPos = i

        return lastPos == 0
