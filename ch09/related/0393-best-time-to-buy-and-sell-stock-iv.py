"""
393. 买卖股票的最佳时机 IV
假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。

设计一个算法来找到最大的利润。你最多可以完成 k 笔交易。

样例
给定价格 = [4,4,6,1,1,4,2,5], 且 k = 2, 返回 6.

挑战
O(nk) 时间序列。

注意事项
你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
"""

"""
为了方便理解，我们把整个股票买卖的过程想象成一个图
操作流程无非就是由一个点指向另外一个点
维护两个状态，一个买入状态，一个卖出状态。
由于题目要求卖出时的最大利润，所以我们选择卖出状态作为我们的dp
定义：dp[i][j] 在第i个trasaction和第j天时，卖出时的最大利润。

买入的最大利润 = 上一个卖出的最大利润 - 买入现在这个股票的价格
buy = max(buy, dp[(i - 1) % 2][j - 1] - prices[j - 1])

所以题目被抽象出来了，我们要找的就是最大路径和的图。
每一次transaction的增多，就相当于在原来的图上做了一个新的优化。
通过这个优化，我们有了不同的连接线路，从而可能增加了最终的利润。

针对transaction，我们有两种case
case1 卖掉股票，找到之前买入股票之后的利润最高点，然后卖出股票得到最大利润
prices[j - 1] + buy
case2 不卖股票，继承上一次的最大利润
dp[i][j - 1]

dp[i][j] = max(dp[i][j - 1], prices[i - 1] + buy)

题目核心在于
1.你要有足够的抽象能力，把这个transaction增加的过程想象成一个不断优化结果的过程
a -> b 可能在一次transaction的时候利润最大，但是两次可能就变成 a -> c -> b
随着transaction的增加，利润是可以基于上一个transaction进行优化的。max(a -> b, a -> c -> b)]
2.要维护两个状态，即图的，点与点之间的连接。
更具体的，就是当前这个股票，是卖还是不卖。
卖的话就要要知道前面买入这个股票最小的代价是在什么时候
不卖的话直接继承就好。
"""


class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if prices is None or len(prices) < 2:
            return 0

        n = len(prices)
        profit = 0
        # 当k很大的时候，时间复杂也会增大。
        # 直接用贪心法处理特殊情况
        if K >= n // 2:
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit
        # write your code here
        dp = [[0 for i in range(n + 1)] for j in range(K + 1)]

        for i in range(1, K + 1):
            # 第一次买是负数
            # buy代表买入的最小代价，即买入之后资产的最大值
            buy = -prices[0]
            for j in range(2, n + 1):
                dp[i][j] = max(dp[i][j - 1], prices[j - 1] + buy)
                # dp[i - 1][j - 1]代表上一次卖出的最大利润，prices[j] 代表买入股票的代价
                # 他们两个相减即代表这次当前买入的净剩值
                # buy = max(x,x)的作用是每次都取到买入的最大净剩值
                buy = max(buy, dp[i - 1][j - 1] - prices[j - 1])

        return dp[-1][-1]