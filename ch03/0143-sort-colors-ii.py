"""
143. 排颜色 II
给定一个有n个对象（包括k种不同的颜色，并按照
1到k进行编号）的数组，将对象进行分类使相同颜色
的对象相邻，并按照1,2，...k的顺序进行排序。

样例
给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在
原地操作使得数组变成[1, 2, 2, 3, 4]

挑战
一个相当直接的解决方案是使用计数排序扫描2遍的算法。
这样你会花费O(k)的额外空间。你否能在不使用额外空间的
情况下完成？

注意事项
You are not suppose to use the library's sort
function for this problem.

k <= n
"""


# 彩虹排序 O(nlogk)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or len(colors) == 0:
            return
        
        self.rainbowSort(colors, 0, len(colors) - 1, 1, k)
        
    def rainbowSort(self, colors, start, end, colorFrom, colorTo):
        if colorFrom == colorTo:
            return
        
        if start >= end:
            return
        
        left, right = start, end
        colorMid = (colorFrom + colorTo) // 2
        
        while left <= right:
            while left <= right and colors[left] <= colorMid:
                left += 1
            while left <= right and colors[right] > colorMid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.rainbowSort(colors, start, right, colorFrom, colorMid)
        self.rainbowSort(colors, left, end, colorMid + 1, colorTo)


# 三指针算法 O(nk)
class Solution1:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        count, left, right = 0, 0, len(colors) - 1
        
        while count < k:
            minColor = float("inf")
            maxColor = float("-inf")
            
            for i in range(left, right + 1):
                minColor = min(minColor, colors[i])
                maxColor = max(maxColor, colors[i])
            
            cur = left
            while cur <= right:
                if colors[cur] == minColor:
                    colors[left], colors[cur] = colors[cur], colors[left]
                    cur += 1
                    left += 1
                elif maxColor > colors[cur] > minColor:
                    cur += 1
                else:
                    colors[right], colors[cur] = colors[cur], colors[right]
                    right -= 1
            
            count += 2


# 计数排序
class Solution2:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        colorNums =[0 for _ in range(k + 1)]
        
        for i in range(len(colors)):
            colorNums[colors[i]] += 1
        
        index = 0
        for i in range(len(colorNums)):
            for j in range(colorNums[i]):
                colors[index] = i
                index += 1


if __name__ == '__main__':
    colors = [3, 2, 2, 1, 4]
    Solution1().sortColors2(colors, 4)
    print(colors)