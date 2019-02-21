"""
105. 复制带随机指针的链表
中文English
给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。

返回一个深拷贝的链表。

挑战
可否使用O(1)的空间
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


# 方法一：倍增原始链表，再解链，空间O(1)
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        self.cloneNodes(head)
        self.connectSiblingNodes(head)
        return self.reconnectNodes(head)

    # 第一步：根据原始链表的每个节点N创建N'
    def cloneNodes(self, head):
        node = head
        while node:
            p_clone = RandomListNode(node.label)
            p_clone.next = node.next
            node.next = p_clone
            node = p_clone.next

    # 第二步：复制随机指针，原来N指向S的随机指针，经过复制，N'指向S'
    def connectSiblingNodes(self, head):
        node = head
        while node:
            p_clone = node.next
            if node.random:
                p_clone.random = node.random.next
            node = p_clone.next

    # 第三步：将得到的长链表拆分为两个链表，奇数位置的节点用next连接，
    # 偶数位置同样单独连接
    def reconnectNodes(self, head):
        node = head
        p_clone_head, p_clone_node = None, None

        if node:
            p_clone_head = p_clone_node = node.next
            node.next = p_clone_node.next
            node = node.next

        while node:
            p_clone_node.next = node.next
            p_clone_node = p_clone_node.next
            node.next = p_clone_node.next
            node = node.next

        return p_clone_head


# 方法二：使用hash，空间O(n)
class Solution1:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dummy = RandomListNode(0)
        last = dummy
        sibling = {}
        while head:
            last.next = RandomListNode(head.label)
            sibling[last.next] = head.random
            last = last.next
            head = head.next

        curr = dummy.next
        while curr:
            curr.random = sibling[curr]
            curr = curr.next

        return dummy.next
