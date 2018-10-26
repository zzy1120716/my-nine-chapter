"""
242. 将二叉树按照层级转化为链表
给一棵二叉树，设计一个算法为每一层的节点建立一个链表。也就是说，
如果一棵二叉树有D层，那么你需要创建D条链表。

样例
对于二叉树：

    1
   / \
  2   3
 /
4
返回3条链表：

[
  1->null,
  2->3->null,
  4->null
]
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
from collections import deque


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []

        result = []
        queue = deque([root])
        # 假节点记录每个链表的起始
        dummy = ListNode(0)
        # 最后的节点，随新节点的插入不断后移
        lastNode = None

        while queue:
            # next指针置空
            dummy.next = None
            lastNode = dummy
            # 通过当前队列长度判断某一层是否已经遍历完
            size = len(queue)
            for i in range(size):
                head = queue.popleft()
                lastNode.next = ListNode(head.val)
                lastNode = lastNode.next

                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)

            result.append(dummy.next)

        return result