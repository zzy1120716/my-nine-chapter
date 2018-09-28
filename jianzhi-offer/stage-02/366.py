"""
366. 斐波纳契数列
查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：

前2个数是 0 和 1 。
第 i 个数是第 i-1 个数和第i-2 个数的和。
斐波纳契数列的前10个数字是：
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

样例
给定 1，返回 0
给定 2，返回 1
给定 10，返回 34

注意事项
The Nth fibonacci number won't exceed the max value of 
signed 32-bit integer in the test cases.
"""

"""
方法一：递归，会超时
"""
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        
        if n == 2:
            return 1
            
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

"""
方法二：非递归
"""
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a