"""
117. 跳跃游戏 II
给出一个非负整数数组，你最初定位在数组的第一个位置。
数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

样例
给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2
(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)
"""
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        p = [0]
        for i in range(len(A) - 1):
            while i + A[i] >= len(p) and len(p) < len(A):
                p.append(p[i] + 1)
        return p[-1]