"""
228. 链表的中点
找链表的中点。

样例
链表 1->2->3 的中点是 2。

链表 1->2 的中点是 1。

挑战
如果链表是一个数据流，你可以不重新遍历链表的情况下
得到中点么？
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if head is None:
            return None
            
        slow, fast = head, head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow