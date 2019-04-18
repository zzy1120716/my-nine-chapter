from collections import deque


# 链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def stringifyLinkedList(head):
    s = ''
    while head:
        s += str(head.val) + ' -> '
        head = head.next
    s += 'None'
    return s


def convertList2LinkedList(values):
    dummy = ListNode(0)
    last = dummy
    for v in values:
        last.next = ListNode(v)
        last = last.next
    return dummy.next


# 二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    # 从list构建二叉树
    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    # 层次遍历
    def level_order_traversal(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    # 先序遍历
    def pre_order_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)

        traversal(self.root)
        return ret

    # 中序遍历
    def in_order_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    # 后序遍历
    def post_order_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret
