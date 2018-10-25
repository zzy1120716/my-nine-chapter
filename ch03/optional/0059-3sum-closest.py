"""
59. 最接近的三数之和
给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。

样例
例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.

挑战
O(n^2) 时间, O(1) 额外空间。

注意事项
只需要返回三元组之和，无需返回三元组本身
"""

"""
双指针
1) 排序
2) for循环最小的数（或最大的数）
3) 剩下的问题就是两数之和最接近的问题了，参考 #533
"""
class Solution:

    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        ans = sys.maxsize
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                three_sum = numbers[left] + numbers[right] + numbers[i]
                if abs(target - three_sum) < abs(ans - target):
                    ans = three_sum

                if three_sum <= target:
                    left += 1
                else:
                    right -= 1

        return ans