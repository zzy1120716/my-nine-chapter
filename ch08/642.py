"""
642. Moving Average from Data Stream
给出一串整数流和窗口大小，计算滑动窗口中所有整数的平均值。

样例
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // 返回 1.00000
m.next(10) = (1 + 10) / 2 // 返回 5.50000
m.next(3) = (1 + 10 + 3) / 3 // 返回 4.66667
m.next(5) = (10 + 3 + 5) / 3 // 返回 6.00000
"""
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        from queue import Queue
        self.queue = Queue()
        self.size = size
        self.sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.sum += val
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum / self.queue.qsize()

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)