"""
428. x的n次幂
实现 pow(x,n)

样例
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1
挑战
O(logn) time

注意事项
不用担心精度，当答案和标准输出差绝对值小于1e-3时都算正确
"""
import sys

class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        
        if n == -sys.maxsize:
            n = -(n + 1)
        
        if n < 0:
            x = 1 / x
            n = -n
            
        if n % 2 == 0:
            temp = self.myPow(x, n // 2)
            return temp * temp
        else:
            temp = self.myPow(x, n // 2)
            return temp * temp * x
            