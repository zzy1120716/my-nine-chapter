"""
35. 翻转链表
翻转一个链表

样例
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

挑战
在原地一次翻转完成
"""


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 方法一：三指针，原地
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head
        
        # null->1->2->3->4->5->null
        #  p    c
        prev = None
        curr = head

        while curr:
            # null->1->2->3->4->5->null
            #  p    c  n
            nxt = curr.next

            # null<-1  2->3->4->5->null
            #  p    c  n
            curr.next = prev

            # null<-1  2->3->4->5->null
            #       c  n
            #       p
            prev = curr

            # null<-1  2->3->4->5->null
            #       p  n
            #          c
            curr = nxt
            
        # null<-1<-2<-3<-4<-5  null
        #                   p  n
        #                      c
        return prev


# 方法二：压栈 + 尾插
class Solution1:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if not head or not head.next:
            return head

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        dummy = ListNode(0)
        last = dummy
        while stack:
            val = stack.pop()
            last.next = ListNode(val)
            last = last.next

        return dummy.next
