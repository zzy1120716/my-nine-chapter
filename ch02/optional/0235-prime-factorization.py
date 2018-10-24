"""
235. 分解质因数
将一个整数分解为若干质因数之乘积

样例
给出 10, 返回 [2, 5].

给出 660, 返回 [2, 2, 3, 5, 11].

注意事项
你需要从小到大排列质因子。
"""
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        factors = []
        i = 2

        while i * i <= num:
            while num % i == 0:
                num = num // i
                factors.append(i)
            i += 1

        if num != 1:
            factors.append(num)

        return factors