"""
141. x的平方根
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

样例
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

挑战
O(log(x))
"""
import math


# 二分法
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        if start * start == x:
            return start
        if end * end == x:
            return end
        return start


class Solution0:
    def sqrt(self, x: int) -> int:
        low, high =  1, x
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 <= x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans


class Solution1:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        return int(math.sqrt(x))


# 牛顿迭代法，令t = sqrt(x), 根据 x = sqrt(x) * sqrt(x)构造不动点
class Solution2:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        guess = 1.0
        while abs(x - guess * guess) > 0.1:
            guess = (x / guess + guess) / 2
        return int(guess)


if __name__ == '__main__':
    print(Solution0().sqrt(3))
    print(Solution0().sqrt(4))
    print(Solution0().sqrt(5))
    print(Solution0().sqrt(10))
