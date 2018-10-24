"""
414. 两个整数相除
将两个整数相除，要求不使用乘法、除法和 mod 运算符。

如果溢出，返回 2147483647 。

样例
给定被除数 = 100 ，除数 = 9，返回 11。
"""
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        # 2147483647
        INT_MAX = (1 << 31) - 1

        if divisor == 0 or (dividend == -INT_MAX - 1 and divisor == -1):
            return INT_MAX

        # 异或，符号不同为-1，相同为1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dvd = abs(dividend)
        dvs = abs(divisor)
        res = 0
        while dvd >= dvs:
            temp, multiple = dvs, 1
            # 左移一位，相当于乘以2
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dvd -= temp
            res += multiple

        return res if sign == 1 else -res