"""
20. 骰子求和
扔 n 个骰子，向上面的数字之和为 S。给定 Given n，请列出所有可能的 S 值及其相应的概率。

样例
给定 n = 1，返回 [ [1, 0.17], [2, 0.17], [3, 0.17], [4, 0.17], [5, 0.17], [6, 0.17]]。

注意事项
You do not care about the accuracy of the result, we will help you to output results.
"""


# DP Solution
# 用dp[i][j]表示有i + 1个骰子的情况下，掷到的和为j的次数。
# 那么intialize这个dp[0][j], j = 1...6的值都为1，然后从i = 1开始做循环。
# i个骰子和i + 1个骰子的差别就是1个骰子（废话），所以再用一个k = 1...6进行遍历，
# 那么i + 1个骰子掷到j + k的次数就是原来dp[i][j + k]的次数加上dp[i - 1][j]。
#
# 这样我们就求得了n个骰子的情况下，每个S出现的次数dp[n - 1][j], j = n...6 * n。
# 那么概率就是每个dp[n - 1][j]除以出现的总次数sum(dp[n - 1][j]).
class Solution:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def dicesSum(self, n):
        # Write your code here
        dp = [[0] * (n * 6 + 1) for _ in range(n)]
        ans = []

        # initialize the dp for n == 1
        for i in range(1, 7):
            dp[0][i] = 1

        # for each dp[i][j + k], it is equal to the
        # number from dp[i - 1][j] + old dp[i][j + k]
        for i in range(n):
            for j in range(i, i * 6 + 1):
                for k in range(1, 7):
                    dp[i][j + k] += dp[i - 1][j]

        # get the total count of number occurs
        total_count = 0
        for i in range(n, n * 6 + 1):
            if dp[n - 1][i] > 0:
                total_count += dp[n - 1][i]

        # get the probability
        for i in range(1, n * 6 + 1):
            if dp[n - 1][i] > 0:
                ans.append((i, dp[n - 1][i] / total_count))

        return ans


if __name__ == '__main__':
    print(Solution().dicesSum(1))
    print(Solution().dicesSum(2))
