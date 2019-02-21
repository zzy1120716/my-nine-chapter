"""
378. 将二叉查找树转换成双链表
中文English
将一个二叉查找树按照中序遍历转换成双向链表。

样例
给定一个二叉查找树：

    4
   / \
  2   5
 / \
1   3
返回 1<->2<->3<->4<->5。
"""


# Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        self.pre = None


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        inorder = []
        self.inorder(root, inorder)

        dummy = DoublyListNode(0)
        curr = dummy
        for val in inorder:
            node = DoublyListNode(val)
            curr.next = node
            node.pre = curr
            curr = curr.next

        return dummy.next

    def inorder(self, root, inorder):
        if not root:
            return
        self.inorder(root.left, inorder)
        inorder.append(root.val)
        self.inorder(root.right, inorder)
