"""
113. 删除排序链表中的重复数字 II
中文English
给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。

样例
给出 1->2->3->3->4->4->5->null，返回 1->2->5->null

给出 1->1->1->2->3->null，返回 2->3->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next != head:
                pre.next = head.next
                head = pre.next
            else:
                head = head.next
                pre = pre.next
        return dummy.next


# 更直观地，单独定义快/慢指针
class Solution2:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        dummy = ListNode(0)
        fast, slow = head, dummy
        slow.next = fast
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next

            if slow.next != fast:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next

        return dummy.next
