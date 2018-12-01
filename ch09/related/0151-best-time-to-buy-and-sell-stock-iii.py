"""
151. 买卖股票的最佳时机 III
假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
设计一个算法来找到最大的利润。你最多可以完成两笔交易。

样例
给出一个样例数组 [4,4,6,1,1,4,2,5], 返回 6

注意事项
你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
"""
import sys


# 两个方向做DP
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n <= 1:
            return 0
        left = [0] * n
        right = [0] * n

        # DP from left to right
        min_v = prices[0]
        for i in range(1, n):
            min_v = min(min_v, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_v)

        # DP from right to left
        max_v = prices[-1]
        for i in range(n - 2, -1, -1):
            max_v = max(max_v, prices[i])
            right[i] = max(right[i + 1], max_v - prices[i])

        result = 0
        for i in range(n):
            result = max(result, left[i] + right[i])
        return result


# 卖的时候最开始的利润是0。第一次买的时候，要钱所以是负数。第一次卖的时候的利润就是第一次买的时候付的钱+赚的钱。
# 第二次买的时候，就是前面赚的钱-第二次买的钱。最后一次卖就是前面剩的钱+利润。
class Solution1:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        buy1 = buy2 = -sys.maxsize-1
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2