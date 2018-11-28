"""
540. 左旋右旋迭代器
给你两个一维向量，实现一个迭代器，交替返回两个向量的元素

样例
v1 = [1, 2]
v2 = [3, 4, 5, 6]
[1, 3, 2, 4, 5, 6]
"""


# 方法一：利用队列存放v1，v2，每次取数，从队头取出一个list（可以是v1或者v2）
# 将取出的list中的第0个元素pop出来，若此list依然非空，则入队到队尾
# 由此实现了轮流取数，取过数的list自动放到队尾，为空则不入队
from collections import deque


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.queue = deque([deque(v) for v in (v1, v2) if v])

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        v = self.queue.popleft()
        value = v.popleft()
        if v:
            self.queue.append(v)
        return value

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.queue) > 0


# 方法二：每次呼叫 next() 時 pop list1，兩列表交換，列表二為空時則不交換
class ZigzagIterator1:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v1 = v1
        self.v2 = v2
        if len(v1) == 0:
            self.v1 = v2

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        val = self.v1.pop(0)
        if len(self.v2) > 0:
            self.v1, self.v2 = self.v2, self.v1
        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.v1) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result


if __name__ == '__main__':
    solution, result = ZigzagIterator([1, 2], [3, 4, 5, 6]), []
    while solution.hasNext():
        result.append(solution.next())
    print(result)
