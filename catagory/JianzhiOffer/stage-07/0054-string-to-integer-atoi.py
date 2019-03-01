"""
54. 转换字符串到整数
中文English
实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。
如果整数超出了32位整数的范围，返回INT_MAX(2147483647)如果是正整数，
或者INT_MIN(-2147483648)如果是负整数。

样例
"10" =>10
"-1" => -1
"123123123123123" => 2147483647
"1.0" => 1
"""
import sys


class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
        str = str.strip()
        n = len(str)
        if n == 0:
            return 0
        start_idx = 0
        sign = 1
        MAX_INT = (1 << 31) - 1
        res = 0
        if str.startswith('-'):
            sign = -1
            start_idx = 1
        elif str.startswith('+'):
            start_idx = 1

        for i in range(start_idx, n):
            if str[i] < '0' or str[i] > '9':
                break
            res = res * 10 + int(str[i])
            if res > sys.maxsize:
                break

        res *= sign
        if res >= MAX_INT:
            return MAX_INT
        if res < MAX_INT * -1:
            return MAX_INT * -1 - 1

        return res


# 方法二：fastest
class Solution2:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        str = str.strip()
        n = len(str)
        if n == 0:
            return 0

        isNeg = False
        start = 0
        if str[0] == '-':
            isNeg = True
            start = 1
        elif str[0] == '+':
            start = 1

        inPrecision = False
        num = 0.0
        precision = 1
        for i in range(start, n):
            ch = str[i]
            if ch == '.':
                if inPrecision:
                    break
                inPrecision = True
                continue

            if not ch.isdigit():
                break

            d = ord(ch) - ord('0')
            if inPrecision:
                precision *= 10

            num *= 10
            num += d

        num /= precision
        if int(num) == num:
            num = int(num)

        if isNeg:
            num = -num

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num


if __name__ == '__main__':
    print(Solution2().atoi('10'))
    print(Solution2().atoi('-1'))
    print(Solution2().atoi('123123123123123'))
    print(Solution2().atoi('1.0'))
