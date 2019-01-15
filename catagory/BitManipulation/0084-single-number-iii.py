"""
84. 落单的数 III
给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。

样例
给出 [1,2,2,3,4,4,5,3]，返回 1和5

挑战
O(n)时间复杂度，O(1)的额外空间复杂度
"""


class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        s = 0
        for x in A:
            s ^= x
        y = s & (-s)

        ans = [0, 0]
        for x in A:
            if (x & y) != 0:
                ans[0] ^= x
            else:
                ans[1] ^= x

        return ans


if __name__ == '__main__':
    print(Solution().singleNumberIII([1, 2, 2, 3, 4, 4, 5, 3]))
