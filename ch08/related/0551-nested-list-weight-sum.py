"""
551. 嵌套列表的加权和
给一个嵌套的整数列表, 返回列表中所有整数由它们的深度加权后的总和.
每一个元素可能是一个整数或一个列表(其元素也可能是整数或列表)

样例
给出列表 [[1,1],2,[1,1]], 返回 10. (4个'1'的深度是 2, 1个'2'的深度是1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
给出列表 [1,[4,[6]]], 返回 27. (1个 '1' 的深度是1, 1个 '4' 的深度是2,
以及1个 '6'的深度是3, 1 + 4 * 2 + 6 * 3 = 27)
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""


# DFS
class Solution(object):

    def __init__(self):
        self.result = 0

    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        self.helper(nestedList, 1)
        return self.result

    def helper(self, nestedList, depth):
        for i in nestedList:
            if i.isInteger():
                self.result += i.getInteger() * depth
            else:
                self.helper(i.getList(), depth + 1)


# 利用栈，类似二叉树的层次遍历
class Solution1(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        if len(nestedList) == 0:
            return 0
        stack = []
        weight_sum = 0
        # 将处在第一层的所有list或integer入栈
        for n in nestedList:
            stack.append((n, 1))
        # 逐个取出
        while stack:
            # list/integer 和 深度
            next_item, depth = stack.pop(0)
            # 是数字，则计算深度乘以权重加入weight_sum
            if next_item.isInteger():
                weight_sum += depth * next_item.getInteger()
            # 是list，则依次入栈
            else:
                for i in next_item.getList():
                    stack.append((i, depth + 1))
        return weight_sum
