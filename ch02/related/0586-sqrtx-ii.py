"""
586. 对x开根II
实现 double sqrt(double x) 并且 x >= 0。
计算并返回x开根后的值。

样例
给出 n = 2 ,返回 1.41421356

注意事项
你不需要在意结果的精确度，我们会帮你输出结果。
"""


# 典型的二分问题
class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if x >= 1:
            start, end = 1, x
        else:
            start, end = x, 1

        while end - start > 1e-10:
            mid = (start + end) / 2
            if mid * mid < x:
                start = mid
            else:
                end = mid

        return start


if __name__ == '__main__':
    print(Solution().sqrt(2))
