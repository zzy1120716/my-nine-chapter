"""
183. 木材加工
有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。
当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

样例
有3根木头[232, 124, 456], k=7, 最大长度为114.

挑战
O(n log Len), Len为 n 段原木中最大的长度

注意事项
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。
无法切出要求至少 k 段的,则返回 0 即可。
"""


# 基于答案值域的二分法
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        if not L:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_pieces(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.get_pieces(L, end) >= k:
            return end
        if self.get_pieces(L, start) >= k:
            return start

        return 0

    def get_pieces(self, L, length):
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces


if __name__ == '__main__':
    print(Solution().get_pieces([232, 124, 456], 7))