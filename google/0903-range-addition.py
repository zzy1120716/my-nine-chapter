"""
903. 范围加法
假设你有一个长度为n的数组，数组的所有元素初始化为0，并且给定k个更新操作。

每个更新操作表示为一个三元组：[startIndex, endIndex, inc]。这个更新操作给子数组
A[startIndex ... endIndex]（包括startIndex和endIndex）中的每一个元素增加 inc。

返回执行k个更新操作后的新数组。

样例
给定：
长度 = 5,
更新操作 =
[
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
]
返回 [-2, 0, 3, 5, 3]

解释:
初始状态：
[ 0, 0, 0, 0, 0 ]
完成 [1, 3, 2]操作后：
[ 0, 2, 2, 2, 0 ]
完成[2, 4, 3]操作后：
[ 0, 2, 5, 5, 3 ]
完成[0, 2, -2]操作后：
[-2, 0, 3, 5, 3 ]
"""

"""
在开头坐标startIndex位置加上inc，而在结束位置加1的地方加上-inc，那么根据题目中的例子，
我们可以得到一个数组，nums = {-2, 2, 3, 2, -2, -3}，然后我们发现对其做累加和就是我们
要求的结果result = {-2, 0, 3, 5, 3}
"""


class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        # Write your code here
        nums = [0 for _ in range(length + 1)]
        for i in range(len(updates)):
            start = updates[i][0]
            end = updates[i][1]
            inc = updates[i][2]
            nums[start] += inc
            nums[end + 1] -= inc
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums[:-1]