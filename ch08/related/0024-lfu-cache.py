"""
24. LFU缓存
LFU是一个著名的缓存算法
实现LFU中的set 和 get

样例
capacity = 3

set(2,2)
set(1,1)
get(2)
>> 2
get(1)
>> 1
get(2)
>> 2
set(3,3)
set(4,4)
get(3)
>> -1
get(2)
>> 2
get(1)
>> 1
get(4)
>> 4
"""
from collections import OrderedDict, defaultdict


# 方法一：LeetCode most upvote Java solution Python edition
# 利用dict实现Java HashMap，利用OrderedDict实现LinkedHashSet
# counts记录访问次数
# get: O(1), set: O(1)
class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.min_val = -1
        self.cap = capacity
        self.vals = {}
        self.counts = {}
        self.lists = defaultdict(OrderedDict)

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if self.cap <= 0:
            return
        if key in self.vals:
            self.vals[key] = value
            self.get(key)
            return

        if len(self.vals) == self.cap:
            evict_key, evict_value = self.lists[self.min_val].popitem(last=False)
            self.vals.pop(evict_key)
            self.counts.pop(evict_key)

        self.vals[key] = value
        self.counts[key] = 1
        self.min_val = 1
        self.lists[1][key] = None

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.vals:
            return -1
        count = self.counts[key]
        self.counts[key] = count + 1
        self.lists[count].pop(key)

        if count == self.min_val and len(self.lists[count]) == 0:
            self.min_val += 1
        self.lists[count + 1][key] = None
        return self.vals[key]


# 方法二：二维双向链表，实现都是用头尾 dummy，容量满了从左上角开始删
# 结构如下：
# D <-> 2 <-> 3 <-> 8 <-> d   |<- freq_list (dll)
#       D     D     D         |<- cache_list (dll)
#       &     &     &
#       n1    n3    n4
#       &     &     &
#       n2    d     n5
#       &           &
#       d           d
# 头跟尾都可以不用 dummy 虚节点而采用 head, tail 变量记录
# 用变量 -> 要麻烦点，需要自己维护变量指向
# 用虚点 -> 头尾要删点的时候，也可以直接把前后接起来就好
# set: O(1), get: O(1)
class LFUCache1:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.D = FreqNode(-1)
        self.d = FreqNode(-1)
        self.D.nxt, self.d.pre = self.d, self.D

    """
    @param: key: An integer
    @param: val: An integer
    @return: nothing
    """
    def set(self, key, val):
        if self.capacity <= 0:
            return

        if key in self.cache:
            self._update_item(key, val)
            return

        if len(self.cache) >= self.capacity:
            self._evict_item()

        self._add_item(key, val)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.cache:
            return -1

        self._update_item(key)
        return self.cache[key].val

    def _add_item(self, key, val):
        cache_node = CacheNode(key, val)
        self.cache[key] = cache_node

        freq_head = self.D.nxt
        if freq_head and freq_head.freq == 0:
            freq_head.append_tail(cache_node)
            return

        freq_head = FreqNode(0)
        freq_head.append_tail(cache_node)
        self.D.after(freq_head)

    def _evict_item(self):
        freq_head = self.D.nxt
        cache_node = freq_head.pop_head()
        self.cache.pop(cache_node.key)

        if freq_head.is_empty():
            freq_head.unlink()

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]

        if val:
            cache_node.val = val

        from_freq = cache_node.freq_node
        to_freq = None

        if from_freq.nxt and from_freq.nxt.freq == from_freq.freq + 1:
            to_freq = from_freq.nxt
        else:
            to_freq = FreqNode(from_freq.freq + 1)
            from_freq.after(to_freq)

        cache_node.unlink()
        to_freq.append_tail(cache_node)

        if from_freq.is_empty():
            from_freq.unlink()


class CacheNode:
    def __init__(self, key, val=None, freq_node=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt

    # to change self in cache nodes
    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre

        self.pre = self.nxt = self.freq_node = None


class FreqNode:
    def __init__(self, freq, pre=None, nxt=None):
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt, self.d.pre = self.d, self.D

    # to change self in freq nodes
    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre

        self.pre = self.nxt = self.D = self.d = None

    # to change self in freq nodes
    def after(self, node):
        node.pre = self
        node.nxt = self.nxt
        self.nxt.pre = node
        self.nxt = node

    # to manage cache nodes
    def is_empty(self):
        return self.D.nxt is self.d

    # to manage cache nodes
    def pop_head(self):
        if self.is_empty():
            return

        head = self.D.nxt
        head.unlink()
        return head

    # to manage cache nodes
    def append_tail(self, node):
        node.freq_node = self
        node.pre = self.d.pre
        node.nxt = self.d
        self.d.pre.nxt = node
        self.d.pre = node


if __name__ == '__main__':
    lfu = LFUCache1(3)
    lfu.set(2, 2)
    lfu.set(1, 1)
    print(lfu.get(2))  # 2
    print(lfu.get(1))  # 1
    print(lfu.get(2))  # 2
    lfu.set(3, 3)
    lfu.set(4, 4)
    print(lfu.get(3))  # -1
    print(lfu.get(2))  # 2
    print(lfu.get(1))  # 1
    print(lfu.get(4))  # 4
