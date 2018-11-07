"""
685. 数据流中第一个唯一的数字
给一个连续的数据流,写一个函数返回终止数字到达时的第一个唯一数字（包括终止数字）,
如果在终止数字前无唯一数字或者找不到这个终止数字, 返回 -1.

样例
给一个数据流 [1, 2, 2, 1, 3, 4, 4, 5, 6] 以及一个数字 5, 返回 3
给一个数据流 [1, 2, 2, 1, 3, 4, 4, 5, 6] 以及一个数字 7, 返回 -1
"""


# LinkList + HashMap 方法
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DataStream:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
        # 保存可能是结果的节点，
        # key为节点值，value为前一个节点，便于删除
        self.num_to_prev = {}
        # 重复的节点值
        self.duplicates = set()

    def remove(self, number):
        prev = self.num_to_prev[number]
        prev.next = prev.next.next
        del self.num_to_prev[number]

        # change tail and prev of next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev

    def add(self, number):
        # 已经存在为该值的节点，不再插入
        if number in self.duplicates:
            return

        # 出现重复，删除dict中的信息
        if number in self.num_to_prev:
            self.remove(number)
            self.duplicates.add(number)
        else:
            node = ListNode(number)
            self.num_to_prev[number] = self.tail
            # 尾插法
            self.tail.next = node
            self.tail = node

    def first_unique(self):
        # 头结点是dummy节点，
        # 头结点的下一个节点的值，就是要返回的结果
        if self.head.next:
            return self.head.next.val
        return -1


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        ds = DataStream()
        for i in range(len(nums)):
            ds.add(nums[i])
            if nums[i] == number:
                return ds.first_unique()
        return -1


if __name__ == '__main__':
    ans = Solution().firstUniqueNumber([1, 2, 2, 1, 3, 4, 4, 5, 6], 5)
    print(ans)
