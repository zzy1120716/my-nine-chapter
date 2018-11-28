"""
528. 摊平嵌套的列表
给你一个嵌套的列表，实现一个迭代器将其摊平。
一个列表的每个元素可能是整数或者一个列表。

样例
给出列表 [[1,1],2,[1,1]]，经过迭代器之后返回 [1,1,2,1,1]。

给出列表 [1,[4,[6]]]，经过迭代器之后返回 [1,4,6]。

注意事项
You don't need to implement the remove method.
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


# 方法一：
# 之前的一个问题是嵌套列表加权和，它需要递归来解决。而这个问题，我们将需要递归来解决它。
# 但由于我们需要一次访问每个NestedInteger，我们将使用堆栈来提供帮助。
# 在构造函数中，我们将所有嵌套列表从后向前推送到堆栈中，因此当我们弹出堆栈时，
# 它会返回第一个元素。 其次，在hasNext()函数中，我们当前查看堆栈中的第一个元素，
# 如果它是一个Integer，我们将返回true并弹出元素。 如果是列表，我们将进一步摊平它。
# 这是展平嵌套列表的迭代版本。同样，我们需要从列表的后面到前面进行迭代。
class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        for i in nestedList[::-1]:
            self.stack.append(i)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            curr = self.stack[-1]
            if curr.isInteger():
                return True
            self.stack.pop()
            for i in curr.getList()[::-1]:
                self.stack.append(i)
        return False


# 简化版本
class NestedIterator1(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = nestedList[::-1]

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        return self.stack.pop().getInteger()

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False


# 方法二：官方答案，创建一个变量保存下个元素
class NestedIterator2(object):

    def __init__(self, nestedList):
        self.next_elem = None
        self.stack = []
        for elem in reversed(nestedList):
            self.stack.append(elem)

    # @return {int} the next element in the iteration
    def next(self):
        if self.next_elem is None:
            self.hasNext()
        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        if self.next_elem:
            return True

        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_elem = top.getInteger()
                return True
            for elem in reversed(top.getList()):
                self.stack.append(elem)
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
