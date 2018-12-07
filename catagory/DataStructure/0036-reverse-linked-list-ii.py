"""
36. 翻转链表 II
翻转链表中第m个节点到第n个节点的部分

样例
给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null

挑战
在原地一次翻转完成

注意事项
m，n满足1 ≤ m ≤ n ≤ 链表长度
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 方法一：利用栈，存储m、n之间的节点值，额外空间O(n-m+1)
class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        start = end = head
        stack = []
        while n > 0 and end:
            if m > 1:
                start = start.next
                m -= 1
            else:
                stack.append(end.val)
            end = end.next
            n -= 1

        while stack:
            val = stack.pop()
            start.val = val
            start = start.next

        return head


# 方法二：官方，原地
class Solution1:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        dummy = ListNode(-1, head)
        mth_prev = self.find_kth(dummy, m - 1)
        mth = mth_prev.next
        nth = self.find_kth(dummy, n)
        nth_next = nth.next
        nth.next = None

        self.reverse(mth)
        mth_prev.next = nth
        mth.next = nth_next
        return dummy.next

    def find_kth(self, head, k):
        for i in range(k):
            if not head:
                return None
            head = head.next
        return head

    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
