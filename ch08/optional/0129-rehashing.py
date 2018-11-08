"""
129. 重哈希
哈希表容量的大小在一开始是不确定的。如果哈希表存储的元素太多（如超过容量的十分之一），
我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。假设你有如下一哈希表：

size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
哈希函数为：

int hashcode(int key, int capacity) {
    return key % capacity;
}
这里有三个数字9，14，21，其中21和9共享同一个位置因为它们有相同的哈希值
1(21 % 4 = 9 % 4 = 1)。我们将它们存储在同一个链表中。

重建哈希表，将容量扩大一倍，我们将会得到：

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
给定一个哈希表，返回重哈希后的哈希表。

样例
给出 [null, 21->9->null, 14->null, null]

返回 [null, 9->null, null, null, null, 21->null, 14->null, null]

注意事项
哈希表中负整数的下标位置可以通过下列方式计算：

C++/Java：如果你直接计算-4 % 3，你会得到-1，你可以应用函数：a % b = (a % b + b) % b
得到一个非负整数。
Python：你可以直接用-1 % 3，你可以自动得到2。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 方法一：维护两个list分别保存拉链的头结点和尾节点
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        CAPACITY = len(hashTable) * 2
        heads = [None] * CAPACITY
        tails = [None] * CAPACITY

        for i in range(len(hashTable)):
            curr = hashTable[i]
            while curr:
                hash_val = curr.val % CAPACITY
                node = ListNode(curr.val)

                if heads[hash_val]:
                    tails[hash_val].next = node
                else:
                    heads[hash_val] = node

                tails[hash_val] = node

                curr = curr.next

        return heads


# 方法二：只用一个list，插入时需要从头开始移动指针
class Solution1:
    # 在链表末尾添加节点
    def addListNode(self, node, number):
        if node.next:
            self.addListNode(node.next, number)
        else:
            node.next = ListNode(number)

    # 两种情况：
    # 该位置为空，直接放入节点
    # 该位置不空，在该位置的链表末尾插入
    def addNode(self, ansHashTable, number):
        hash_val = number % len(ansHashTable)
        if not ansHashTable[hash_val]:
            ansHashTable[hash_val] = ListNode(number)
        else:
            self.addListNode(ansHashTable[hash_val], number)

    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        HASH_SIZE = 2 * len(hashTable)
        ansHashTable = [None] * HASH_SIZE
        for item in hashTable:
            curr = item
            while curr:
                self.addNode(ansHashTable, curr.val)
                curr = curr.next
        return ansHashTable


if __name__ == '__main__':
    hashTable = [None] * 4
    n1 = ListNode(9)
    n2 = ListNode(14)
    n3 = ListNode(21)
    n3.next = n1
    hashTable[1] = n3
    hashTable[2] = n2
    ansHashTable = Solution().rehashing(hashTable)
    print(ansHashTable)