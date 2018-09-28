"""
140. 快速幂
计算an % b，其中a，b和n都是32位的非负整数。

样例
例如 231 % 3 = 2

例如 1001000 % 1000 = 0

挑战
O(logn)
"""

# recursion
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
            
        if n % 2 == 0:
            temp = self.fastPower(a, b, n // 2)
            return temp * temp % b
        else:
            temp = self.fastPower(a, b, n // 2)
            return temp * temp * a % b

# non-recursion
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = ans * a % b
                n -= 1
            a = a * a % b
            n /= 2
        return ans % b