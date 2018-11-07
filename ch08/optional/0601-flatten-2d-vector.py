"""
601. 摊平二维向量
设计一个迭代器来实现摊平二维向量的功能

样例
给一个二维向量

[
  [1,2],
  [3],
  [4,5,6]
]
通过重复调用，直到hasNext返回false，下一个返回的元素的顺序应该是：[1,2,3,4,5,6]。
"""


# 方法一：无法保证在调用next前，先调用了hasNext
class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row = 0
        self.col = 0
        self.vec2d = vec2d

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.col += 1
        return self.vec2d[self.row][self.col - 1]

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.vec2d)


# 方法二：记录横纵坐标。这个版本的代码复杂一些，但是无所谓 next 和 hasNext 的调用顺序和次数。
class Vector2D2(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.row, self.col = 0, -1
        self.next_elem = None

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.next_elem is None:
            self.hasNext()
        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.next_elem:
            return True

        self.col += 1
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0

        if self.row < len(self.vec2d) and self.col < len(self.vec2d[self.row]):
            self.next_elem = self.vec2d[self.row][self.col]
            return True

        return False


# 方法三：增加remove方法
class Vector2D3(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.array = vec2d
        self.row = 0
        self.col = 0
        self.num_row = len(self.array)

    # @return {int} a next element
    def next(self):
        # Write your code here
        res = self.array[self.row][self.col]
        self.col += 1
        if self.col == len(self.array[self.row]):
            self.row += 1
            self.col = 0
        return res

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.array is None or len(self.array) == 0:
            return False

        while self.row < self.num_row and (self.array[self.row] is None or len(self.array[self.row]) == 0):
            self.row += 1

        return self.row < self.num_row

    def remove(self):
        # case 1: if the element to remove is the last element of the row
        if self.col == 0:
            last_row = self.row - 1
            last_col = len(self.array[last_row]) - 1

        # case 2: if the element to remove is not the last element
        else:
            last_col = self.col - 1
            last_row = self.row
            self.col -= 1

        # if the list to remove has no element
        if len(self.array[last_row]) == 0:
            last_row -= 1

        # remove the element
        self.array[last_row].pop(last_col)


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


if __name__ == '__main__':
    i, v = Vector2D3([
        [1, 2],
        [3],
        [4, 5, 6]
    ]), []
    target = 3
    while i.hasNext():
        num = i.next()
        if num == target:
            i.remove()
    i.row = 0
    i.col = 0
    while i.hasNext():
        v.append(i.next())
    print(v)
