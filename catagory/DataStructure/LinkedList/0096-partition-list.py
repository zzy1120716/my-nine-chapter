"""
96. 链表划分
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。

样例
给定链表 1->4->3->2->5->2->null，并且 x=3

返回 1->2->2->4->3->5->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 小于x的节点，大于x的节点，分别组成一个链表
# 遍历完原始链表后，将两个链表首尾相接即可
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return head

        ldummy, rdummy = ListNode(0), ListNode(0)
        left, right = ldummy, rdummy

        while head is not None:
            if head.val < x:
                # 尾插
                left.next = head
                left = head
            else:
                # 尾插
                right.next = head
                right = head
            head = head.next

        right.next = None
        left.next = rdummy.next
        return ldummy.next
