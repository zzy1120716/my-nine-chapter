"""
165. 合并两个排序链表
将两个排序链表合并为一个新的排序链表

样例
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    t1 = l1
    t1.next = ListNode(3)
    t1 = t1.next
    t1.next = ListNode(8)
    t1 = t1.next
    t1.next = ListNode(11)
    t1 = t1.next
    t1.next = ListNode(15)
    t1 = t1.next
    l2 = ListNode(2)
    ans = Solution().mergeTwoLists(l1, l2)
    print(ans)