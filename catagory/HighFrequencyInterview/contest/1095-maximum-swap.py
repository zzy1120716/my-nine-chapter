"""
1095. 最大的交换
给定一个非负整数，你可以交换两个数位至多一次来获得最大的合法的数。
返回最大的合法的你能够获得的数。

样例
样例1:

输入: 2736
输出: 7236
解释: 交换数字2和数字7.
样例2:

输入: 9973
输出: 9973
解释: 不用交换.
注意事项
给定的数字在 [0, 10^8] 内。
"""


# 暴力法，注意交换数位比较后，将list还原
class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        l = list(str(num))
        vmax = l[:]
        for i in range(len(l)):
            for j in range(i, len(l)):
                l[i], l[j] = l[j], l[i]
                if l > vmax:
                    vmax = l[:]
                l[i], l[j] = l[j], l[i]
        return int(''.join(vmax))
