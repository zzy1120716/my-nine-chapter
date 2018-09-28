"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is not None:
            slow, fast = head, head.next
            while fast is not None and fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if slow is None or fast is None:
                    return False
                if slow == fast:
                    return True
        
        return False