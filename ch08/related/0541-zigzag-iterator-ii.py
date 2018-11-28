"""
541. 左旋右旋迭代器 II
k 个一维向量，循环地返回向量中的元素

样例
k = 3

[1,2,3]
[4,5,6,7]
[8,9]
返回 [1,4,8,2,5,9,3,6,7].
"""
from collections import deque


# 思路同#540，维护一个队列存放所有非空list
class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = deque([deque(v) for v in vecs if v])

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


# 方法二：删除法，用一指针指到next的sublist，每次做pop，当sublist为空，
# 删除，重算指针（若需要保持原数据，则可先进行复制）
class ZigzagIterator2Two:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.vecs = vecs
        self.pointer = 0
        i = 0
        while i < len(vecs):
            if len(vecs[i]) == 0:
                del vecs[i]
            else:
                i += 1

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        val = self.vecs[self.pointer][0]
        del self.vecs[self.pointer][0]

        if len(self.vecs[self.pointer]) == 0:
            del self.vecs[self.pointer]
        else:
            self.pointer += 1

        if len(self.vecs) > 0:
            self.pointer %= len(self.vecs)

        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return len(self.vecs) > 0


# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result


if __name__ == '__main__':
    solution, result = ZigzagIterator2Two([[1, 2, 3], [4, 5, 6, 7], [8, 9]]), []
    while solution.hasNext():
        result.append(solution.next())
    print(result)
    assert result == [1, 4, 8, 2, 5, 9, 3, 6, 7]
