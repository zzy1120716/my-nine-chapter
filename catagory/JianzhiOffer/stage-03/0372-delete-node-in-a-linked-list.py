"""
372. 在O(1)时间复杂度删除链表节点
中文English
给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在 O(1) 时间复杂度删除该链表节点。

样例
样例 1：

输入：
1->2->3->4->null
3
输出：
1->2->4->null
样例 2：

输入：
1->3->5->null
3
输出：
1->5->null
"""


# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        node.val = node.next.val
        node.next = node.next.next
