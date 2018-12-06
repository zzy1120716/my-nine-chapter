"""
116. 跳跃游戏
给出一个非负整数数组，你最初定位在数组的第一个位置。　　　
数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　
判断你是否能到达数组的最后一个位置。

样例
A = [2,3,1,1,4]，返回 true.
A = [3,2,1,0,4]，返回 false.

注意事项
这个问题有两个方法，一个是贪心和 动态规划。
贪心方法时间复杂度为O（N）。
动态规划方法的时间复杂度为为O（n^2）。
我们手动设置小型数据集，使大家可以通过测试的两种方式。
这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。
如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。
"""
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def canJump(self, A):
        # write your code here
        p = 0
        ans = 0
        for item in A[:-1]:
            ans = max(ans, p + item)
            if ans <= p:
                return False
            p += 1
        return True