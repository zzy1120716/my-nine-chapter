"""
149. 买卖股票的最佳时机
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。

样例
给出一个数组样例 [3,2,3,1,2], 返回 1
"""


# 找到最低的价格，找当前价格和最低价格差的最大值，就是最好的卖出时机
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(price - min_price, max_profit)

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([3, 2, 3, 1, 2]))
    print(Solution().maxProfit([3, 2, 3, 4, 2]))
    print(Solution().maxProfit([4, 2, 3, 1, 2]))
