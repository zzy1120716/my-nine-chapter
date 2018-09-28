"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None
        
        nowA = headA
        
        # 构造带环链表
        while nowA.next is not None:
            nowA = nowA.next
        nowA.next = headB
        
        result = self.listCycleII(headA)
        
        nowA = None
        return result
        
    # 问题转化为带环链表问题
    def listCycleII(self, head):
        slow, fast = head, head.next
        # 开始追及
        while fast != slow:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            
        # 追上之后，慢指针回到起点，快、慢指针都走一步，再次相遇的位置，就是环的起始节点
        slow = head
        fast = fast.next
        while slow != fast:
            fast = fast.next
            slow = slow.next
            
        return slow
        