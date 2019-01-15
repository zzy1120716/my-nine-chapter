"""
82. 落单的数
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例
给出 [1,2,2,1,3,4,3]，返回 4

挑战
一次遍历，常数级的额外空间复杂度
"""


# 异或“^”，一个数异或上不同于自己的数还是它自己，相同为0
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        ans = 0
        for x in A:
            ans = ans ^ x
        return ans


if __name__ == '__main__':
    print(Solution().singleNumber([1, 2, 2, 1, 3, 4, 3]))
