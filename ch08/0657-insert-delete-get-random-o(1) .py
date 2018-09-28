"""
657. Insert Delete GetRandom O(1)
设计一个数据结构实现在平均 O(1) 的复杂度下执行以下所有的操作。

insert(val): 如果这个元素不在set中，则插入。

remove(val): 如果这个元素在set中，则从set中移除。

getRandom: 随机从set中返回一个元素。每一个元素返回的可能性必须相同。

样例
// 初始化空集set
RandomizedSet randomSet = new RandomizedSet();

// 1插入set中。返回正确因为1被成功插入
randomSet.insert(1);

// 返回错误因为2不在set中
randomSet.remove(2);

// 2插入set中，返回正确，set现在有[1,2]。
randomSet.insert(2);

// getRandom 应该随机的返回1或2。
randomSet.getRandom();

// 从set中移除1，返回正确。set现在有[2]。
randomSet.remove(1);

// 2已经在set中，返回错误。
randomSet.insert(2);

// 因为2是set中唯一的数字，所以getRandom总是返回2。
randomSet.getRandom();
"""
import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.nums, self.pos = [], {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()