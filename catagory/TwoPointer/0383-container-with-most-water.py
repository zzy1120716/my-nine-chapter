"""
383. 装最多水的容器
中文English
给定 n 个非负整数 a1, a2, ..., an, 每个数代表了坐标中的一个点 (i, ai)。画 n 条垂直线，
使得 i 垂直线的两个端点分别为(i, ai)和(i, 0)。找到两条线，使得其与 x 轴共同构成一个容器，
以容纳最多水。

样例 1:
输入: [1, 3, 2]
输出: 2
解释:
选择 a1, a2, 容量为 1 * 1 = 1
选择 a1, a3, 容量为 1 * 2 = 2
选择 a2, a3, 容量为 2 * 1 = 2

样例 2:
输入: [1, 3, 2, 2]
输出: 4
解释:
选择 a1, a2, 容量为 1 * 1 = 1
选择 a1, a3, 容量为 1 * 2 = 2
选择 a1, a4, 容量为 1 * 3 = 3
选择 a2, a3, 容量为 2 * 1 = 2
选择 a2, a4, 容量为 2 * 2 = 4
选择 a3, a4, 容量为 2 * 1 = 2

注意事项
容器不可倾斜。
"""


class Solution:
    def maxArea(self, heights):
        left, right = 0, len(heights) - 1
        area = 0
        while left < right:
            area = max(area, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area


if __name__ == '__main__':
    # 49
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

