"""
174. 删除链表中倒数第n个节点
中文English
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

样例
Example 1:
Input: list = 1->2->3->4->5->null， n = 2
Output: 1->2->3->5->null

Example 2:
Input:  list = 5->4->3->2->1->null, n = 2
Output: 5->4->3->1->null

挑战
O(n)时间复杂度

注意事项
链表中的节点个数大于等于n
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(n):
            if not head:
                return
            head = head.next
        while head:
            pre = pre.next
            head = head.next
        pre.next = pre.next.next
        return dummy.next
