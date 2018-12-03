"""
12. 带最小值操作的栈
实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。

你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。

样例
如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1

注意事项
如果堆栈中没有数字则不能进行min方法的调用
"""


# 建立一个额外的栈min_stack，栈顶永远是当前stack的最小值
# 1）入栈时，若要入栈的元素小于栈顶元素，则进入min_stack，作为新的栈顶
# 2）出栈时，若stack的栈顶元素等于min_stack的栈顶元素，说明最小值元素出栈，两个栈同时pop
# 3）MinStack.min方法，直接返回min_stack栈顶元素即可，时间复杂度O(n)
class MinStack:

    def __init__(self):
        # do initialization if necessary
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        number = self.stack.pop()
        if number == self.min_stack[-1]:
            self.min_stack.pop()
        return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]


if __name__ == '__main__':
    ms = MinStack()
    ms.push(1)
    print(ms.pop())     # 1
    ms.push(2)
    ms.push(3)
    print(ms.min())     # 2
    ms.push(1)
    print(ms.min())     # 1
