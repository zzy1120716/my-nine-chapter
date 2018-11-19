"""
380. 两个链表的交叉
请写一个程序，找到两个单链表最开始的交叉节点。

样例
下列两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始交叉。

挑战
需满足 O(n) 时间复杂度，且仅用 O(1) 内存。

注意事项
如果两个链表没有交叉，返回null。
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
"""

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
        