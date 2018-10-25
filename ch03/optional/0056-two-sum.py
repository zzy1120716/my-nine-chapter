"""
56. 两数之和
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。
注意这里下标的范围是 0 到 n-1。

样例
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].

挑战
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
注意事项
你可以假设只有一组答案。
"""

"""
方法一：hash索引，python中用dict实现
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]], i]
            hash[numbers[i]] = i
        return [-1, -1]


"""
方法二：双指针
"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i, a in enumerate(numbers):
            for j, b in enumerate(numbers[i + 1:]):
                if a + b == target:
                    return [i, j + i + 1]
        return [-1, -1]