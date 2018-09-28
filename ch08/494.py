"""
494. 双队列实现栈
利用两个队列来实现一个栈的功能

样例
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
"""
class Stack:
    
    def __init__(self):
        from queue import Queue
        self.q1 = Queue(); self.q2 = Queue()
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return item
        
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        item = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        self.q1.put(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.q1.empty()