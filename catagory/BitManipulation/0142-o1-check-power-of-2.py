"""
142. O(1)时间检测2的幂次
用 O(1) 时间检测整数 n 是否是 2 的幂次。

样例
n=4，返回 true;

n=5，返回 false.

挑战
O(1) time
"""


# 不断乘二（左移一位），当与n相等时，则是2的幂，
# 输入一定小于 2 ^ 31，所以可以限制循环的次数。
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans << 1
        return False
