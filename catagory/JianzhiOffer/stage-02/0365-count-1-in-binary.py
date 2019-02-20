"""
365. 二进制中有多少个1
中文English
计算在一个 32 位的整数的二进制表示中有多少个 1。

样例
样例 1：

输入：32
输出：1
解释：
32(100000)，返回 1。
样例 2：

输入：5
输出：2
解释：
5(101)，返回 2。
挑战
如果整数有 n 位，并且有 m 位个 1。你能在 O(m) 的时间内解决它吗？
"""


class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        ones = 0
        for i in range(32):
            # % 2
            ones += num & 1
            # // 2
            num >>= 1
        return ones


if __name__ == '__main__':
    # 32
    print(Solution().countOnes(-1))
    # 1
    print(Solution().countOnes(256))
