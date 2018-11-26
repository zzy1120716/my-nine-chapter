"""
211. 字符串置换
给定两个字符串，请设计一个方法来判定其中一个字符串是否为另一个字符串的置换。

置换的意思是，通过改变顺序可以使得两个字符串相等。

样例
"abc" 为 "cba" 的置换。

"aabc" 不是 "abcc" 的置换。
"""


class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        return sorted(A) == sorted(B)


# 用dict来装A中的字符跟出现的次数，
# 然后出现在b的减一
# 若有值不为0，返回False
class Solution1:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        if len(A) != len(B):
            return False

        d = {}

        for a in A:
            if a in d:
                d[a] += 1
                continue
            d[a] = 1

        for b in B:
            if b not in B:
                return False
            d[b] -= 1

        for v in d.values():
            if v != 0:
                return False

        return True
