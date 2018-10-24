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

"""
其实就是求x : x + (x - 1) + (x - 2)+ ... + 1 >= n, 即 (x + 1) * x // 2 >= n
先倍增法找右边界，然后二分法找first position >= n， 类似Search in a Big Sorted Array
"""
class Solution:
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