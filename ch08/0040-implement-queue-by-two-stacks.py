"""
40. 用栈实现队列
正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。

样例
比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2

挑战
仅使用两个栈来实现它，不使用任何其他数据结构，push，pop 和 top的复杂度都应该是均摊O(1)的
"""

"""
方法一
"""
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ret

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        ret = self.stack2.pop()
        self.stack2.append(ret)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return ret

"""
方法二：精简版
"""
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        self.top()
        return self.stack2.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


"""
方法三：不使用pop
"""
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.in_stack, self.out_stack, self.out_index = [], [], -1

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.in_stack += [element]

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        res, self.out_index = self.top(), self.out_index - 1
        return res

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        self.outSafe()
        return self.out_stack[self.out_index]

    def outSafe(self):
        if self.out_index == -1:
            self.out_stack, size = [], len(self.in_stack)
            for i in range(size):
                self.out_stack.append(self.in_stack[size - i - 1])
            self.in_stack, self.out_index = [], len(self.out_stack) - 1