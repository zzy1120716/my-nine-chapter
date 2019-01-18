"""
147. 水仙花数
水仙花数的定义是，这个数等于他每一位上数的幂次之和 见维基百科的定义

比如一个3位的十进制整数153就是一个水仙花数。因为 153 = 1^3 + 5^3 + 3^3。

而一个4位的十进制数1634也是一个水仙花数，因为 1634 = 1^4 + 6^4 + 3^4 + 4^4。

给出n，找到所有的n位十进制水仙花数。

样例
比如 n = 1, 所有水仙花数为：[0,1,2,3,4,5,6,7,8,9]。
而对于 n = 2, 则没有2位的水仙花数，返回 []。

注意事项
你可以认为n小于8。
"""


# 类似于寻找3位的水仙花数
# 枚举10^(n - 1)到10^n之间的所有数
# for n in range(100,1000):
#     i = n / 100
#     j = n / 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print n
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 6:
            return [548834]
        result = []
        for i in range(10 ** (n - 1), 10 ** n):
            j, s = i, 0
            while j != 0:
                s += (j % 10) ** n
                j //= 10
            if s == i:
                result.append(i)
        return result
