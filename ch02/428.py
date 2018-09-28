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
            