"""
83. 落单的数 II
给出3*n + 1 个非负整数，除其中一个数字之外其他每个数字均出现三次，找到这个数字。

样例
给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4

挑战
一次遍历，常数级的额外空间复杂度
"""


# 方法一：
# 用一个32位的数的每一位表示某一位出现几次，出现3次就给它归零
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        if not A:
            return -1
        result = 0
        bits = [0 for _ in range(32)]
        for i in range(32):
            for j in range(len(A)):
                bits[i] += A[j] >> i & 1
                bits[i] %= 3
            result |= (bits[i] << i)
        return result


# 方法二：
class Solution1:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
        ones, twos = 0, 0
        for i in range(len(A)):
            ones = (ones ^ A[i]) & ~twos
            twos = (twos ^ A[i]) & ~ones

        return ones


if __name__ == '__main__':
    print(Solution1().singleNumberII([1, 1, 2, 3, 3, 3, 2, 2, 4, 1]))
