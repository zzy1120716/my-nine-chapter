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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return None
        
        slow, fast = head, head.next
        # 追上之前，快指针走两步，慢指针走一步
        while fast != slow:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            
        # 追上之后，快指针回到起点，快、慢指针都走一步，再次相遇的位置，就是环的起始节点
        while head != slow.next:
            head = head.next
            slow = slow.next
            
        return head