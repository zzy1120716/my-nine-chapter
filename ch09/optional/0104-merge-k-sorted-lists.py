"""
104. Merge K Sorted Lists
合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。

样例
给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null
"""


# Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 方法一：分治法
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists or len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwo(left, right)

    def mergeTwo(self, l1, l2):
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


# 方法二：堆
import heapq


class Solution1:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        if not lists or len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]

        values = []
        for l in lists:
            while l:
                heapq.heappush(values, l.val)
                l = l.next

        dummy = ListNode(0)
        tail = dummy
        while values:
            min_val = heapq.heappop(values)
            tail.next = ListNode(min_val)
            tail = tail.next

        return dummy.next


if __name__ == '__main__':
    print(Solution1().mergeKLists([None, ListNode(1)]))