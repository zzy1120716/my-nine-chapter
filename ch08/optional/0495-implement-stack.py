"""
495. 实现栈
实现一个栈，可以使用除了栈之外的数据结构

样例
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
"""


# 用list作为队列实现栈
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.queue == []
