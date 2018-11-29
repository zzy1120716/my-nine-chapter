"""
134. LRU缓存策略
为最近最少使用（LRU）缓存策略设计一个数据结构，
它应该支持以下操作：获取数据（get）和写入数据（set）。

获取数据get(key)：如果缓存中存在key，则获取其数据值
（通常是正数），否则返回-1。

写入数据set(key, value)：如果key还没有在缓存中，则写入
其数据值。当缓存达到上限，它应该在写入新数据之前删除最
近最少使用的数据用来腾出空闲位置。
"""


# 方法一：令狐冲Java版本翻译过来的
class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do initialization if necessary
        self.capacity = capacity
        self.size = 0
        self.key_to_prev = {}
        self.dummy = LinkedNode(0, 0)
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: nothing
    """
    def move_to_tail(self, key):
        prev = self.key_to_prev[key]
        curt = prev.next

        if self.tail == curt:
            return

        prev.next = prev.next.next
        self.tail.next = curt

        if prev.next:
            self.key_to_prev[prev.next.key] = prev
        self.key_to_prev[curt.key] = self.tail

        self.tail = curt

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1

        self.move_to_tail(key)
        # the key has been moved to the end
        return self.tail.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if self.get(key) != -1:
            prev = self.key_to_prev[key]
            prev.next.val = value
            return

        if self.size < self.capacity:
            self.size += 1
            curt = LinkedNode(key, value)
            self.tail.next = curt
            self.key_to_prev[key] = self.tail
            self.tail = curt
            return

        first = self.dummy.next
        del self.key_to_prev[first.key]

        first.key = key
        first.val = value
        self.key_to_prev[key] = self.dummy

        self.move_to_tail(key)


# 方法二：九章python
class LRUCache1:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


# 方法三：使用高级数据结构，OrderedDict
from collections import OrderedDict


class LRUCache2:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.cache = OrderedDict()

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        # pop value and insert to the bottom of queue
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            # last为True时pop规则为FILO，last为False时pop规则为FIFO
            self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.set(2, 1)
    lru.set(1, 1)
    print(lru.get(2))
    lru.set(4, 1)
    print(lru.get(1))
    print(lru.get(2))