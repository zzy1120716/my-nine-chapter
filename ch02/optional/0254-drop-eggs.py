"""
254. Drop Eggs
There is a building of n floors. If an egg drops from the k th floor or above,
it will break. If it's dropped from any floor below, it will not break.

You're given two eggs, Find k while minimize the number of drops for the worst case.
Return the number of drops in the worst case.

样例
Given n = 10, return 4.
Given n = 100, return 14.

说明
For n = 10, a naive way to find k is drop egg from 1st floor, 2nd floor ... kth floor.
But in this worst case (k = 10), you have to drop 10 times.

Notice that you have two eggs, so you can drop at 4th, 7th & 9th floor, in the worst
case (for example, k = 9) you have to drop 4 times.
"""


# 方法一：公式法
# https://blog.csdn.net/shaya118/article/details/40823225
# 先解释为什么10层楼的时候用4次
# 先从floor4扔
# break了，就需要用另一个从floor1开始往上找，最多用3次，一共4次
# 没有break，再从floor7扔
# break了，就需要用另一个从floor5开始往上找，最多用2次，一共是4次
# 没有break， 再从floor9扔
# break了，就需要用另一个从floor8开始往上找，最多用1次，一共是4次
# 没有break，确定是 k = 10
# 倒过来看就是一个等差数列的过程：[10], [9, 8], [7, 6, 5], [4, 3, 2, 1]
# 所以累加的方法就是找到最小的m，使得1到m的公差为1的等差数列的和大于n
#
# 然后直接求解就是，等差数列的和为 m * (m + 1) / 2,
# 令其大于等于 n，
# 得到 m ** 2 + m - 2n >= 0,
# 然后用一元二次方程求解公式取正值，
# 再取ceil()就可以了
import math


class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    # 累加
    def dropEggs(self, n):
        # write your code here
        res = sum = 1
        while sum < n:
            res += 1
            sum += res
        return res

    # 直接求解
    def dropEggs1(self, n):
        return math.ceil((math.sqrt(8 * n) - 1) / 2)


# 方法二：二分
# 其实就是求x : x + (x - 1) + (x - 2)+ ... + 1 >= n, 即 (x + 1) * x // 2 >= n
# 先倍增法找右边界，然后二分法找first position >= n， 类似Search in a Big Sorted Array
class Solution1:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        # write your code here
        index = 1
        while index * (index + 1) // 2 < n:
            index = index * 2

        start, end = 1, index
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * (mid + 1) // 2 >= n:
                end = mid
            else:
                start = mid

        if start * (start + 1) // 2 >= n:
            return start
        else:
            return end