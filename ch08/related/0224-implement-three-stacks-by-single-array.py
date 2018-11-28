"""
224. 用一个数组实现三个栈
用一个数组实现三个栈。你可以假设这三个栈都一样大并且足够大。
你不需要担心如果一个栈满了之后怎么办。

样例
ThreeStacks(5)  // create 3 stacks with size 5 in single array. stack index from 0 to 2
push(0, 10) // push 10 in the 1st stack.
push(0, 11)
push(1, 20) // push 20 in the 2nd stack.
push(1, 21)
pop(0) // return 11
pop(1) // return 21
peek(1) // return 20
push(2, 30)  // push 30 in the 3rd stack.
pop(2) // return 30
isEmpty(2) // return true
isEmpty(0) // return false
"""


# 方法一：官方Java版改写
class StackNode:
    def __init__(self, p, v, n):
        self.value = v
        self.prev = p
        self.next = n


class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.stack_size = size
        self.index_used = 0
        self.stack_pointer = [-1] * 3
        self.buffer = [0] * (size * 3)

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        last_index = self.stack_pointer[stackNum]
        self.stack_pointer[stackNum] = self.index_used
        self.index_used += 1
        self.buffer[self.stack_pointer[stackNum]] = StackNode(last_index, value, -1)

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        value = self.buffer[self.stack_pointer[stackNum]].value
        last_index = self.stack_pointer[stackNum]
        if last_index != self.index_used - 1:
            self.swap(last_index, self.index_used - 1, stackNum)

        self.stack_pointer[stackNum] = self.buffer[self.stack_pointer[stackNum]].prev
        if self.stack_pointer[stackNum] != -1:
            self.buffer[self.stack_pointer[stackNum]].next = -1

        self.buffer[self.index_used - 1] = None
        self.index_used -= 1
        return value

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        return self.buffer[self.stack_pointer[stackNum]].value

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return self.stack_pointer[stackNum] == -1

    def swap(self, last_index, top_index, stackNum):
        if self.buffer[last_index].prev == top_index:
            self.buffer[last_index].value, self.buffer[top_index].value = self.buffer[top_index].value, self.buffer[
                last_index].value
            tp = self.buffer[top_index].prev
            if tp != -1:
                self.buffer[tp].next = last_index
            self.buffer[last_index].prev = tp
            self.buffer[last_index].next = top_index
            self.buffer[top_index].prev = last_index
            self.buffer[top_index].next = -1
            self.stack_pointer[stackNum] = top_index
            return

        lp = self.buffer[last_index].prev
        if lp != -1:
            self.buffer[lp].next = top_index

        tp = self.buffer[top_index].prev
        if tp != -1:
            self.buffer[tp].next = last_index

        tn = self.buffer[top_index].next
        if tn != -1:
            self.buffer[tn].prev = last_index
        else:
            for i in range(3):
                if self.stack_pointer[i] == top_index:
                    self.stack_pointer[i] = last_index

        self.buffer[last_index], self.buffer[top_index] = self.buffer[top_index], self.buffer[last_index]
        self.stack_pointer[stackNum] = top_index


# 方法二：建立一个 dict 记录每个栈的栈顶位置。
# 由于使用了 dict， 所以查找起来速度比较快。
class ThreeStacks1:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.stack = [None] * (size * 3)
        self.index = {0: 0, 1: size, 2: 2 * size}

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        if self.stack[self.index[stackNum]] is None:
            self.stack[self.index[stackNum]] = value
        else:
            self.index[stackNum] += 1
            self.stack[self.index[stackNum]] = value

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        result = self.stack[self.index[stackNum]]
        self.stack[self.index[stackNum]] = None
        self.index[stackNum] -= 1
        return result

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        return self.stack[self.index[stackNum]]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        if self.stack[self.index[stackNum]] is None:
            return True
        else:
            return False


if __name__ == '__main__':
    ts = ThreeStacks1(5)
    ts.push(0, 10)
    ts.push(0, 11)
    ts.push(1, 20)
    ts.push(1, 21)
    print(ts.pop(0))  # 11
    print(ts.pop(1))  # 21
    print(ts.peek(1))  # 20
    ts.push(2, 30)
    print(ts.pop(2))  # 30
    print(ts.isEmpty(2))  # true
    print(ts.isEmpty(0))  # false
