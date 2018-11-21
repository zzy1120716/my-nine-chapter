"""
67. 二叉树的中序遍历
给出一棵二叉树,返回其中序遍历

样例
给出二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [1,3,2].

挑战
你能使用非递归算法来实现么?
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


# 递归
class Solution:

    result = []

    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.result = []
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.result.append(root.val)
        self.helper(root.right)


# 非递归
# 1. 添加所有最左边节点到栈。
# 2. pop stack 然后添加到结果。
# 3. 查找当前node的右边节点是否为空， 如果不为空，重复step 1。
#
# 这个算法包括了两种操作：第一个操作是把一整条向左的path都存入到stack里面，第二个操作是
# 寻找先驱节点。这个算法用到的一个重要的性质是：对于一个右子树，先驱节点到达它的方式一定是，
# 先向左一下，（到达进入右子树，但却已经被访问过的那个节点），再向右进入右子树，所以利用这
# 个性质，所有stack[-1] == node的节点其实都是已经被printed的节点了，不是真正的先驱节点。
class Solution1:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        stack = []
        result = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            result.append(node.val)

            if not node.right:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return result


# 利用None的次数来标记父节点。第一次向stack填入None的时候，都代表进入情况2（没有左节点了），
# 这个时候pop 掉stack 并print，进入这个被print 节点的右子树，然后第二次出现None的时候，是
# 情况2.2（右子树也空了），这个时候pop出来的就是真正的先驱节点。那个已经被printed的先驱节
# 点，在第一次出现None的时候已经被pop掉了。
class Solution2:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        stack = []
        curr = root
        while curr or stack:
            if not curr:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return result


# Morris算法
# 把一个子树的最右边的节点（最后一个被访问的节点）的右节点，连到它的先驱节点上。这样就避免
# 了找先驱节点的麻烦，相当于反向的思维解决了问题。算法是对于每一个节点，第一步是找它是谁的
# 先驱节点，方法和2类似，就是找它左子树的最右边，首先如果没有左子树，直接print 然后向右走
# 就行。然后要分两种情况：
# 1. 发现它左子树最右边是None，就把这个None改成它自己，向左走；
# 2. 如果左子树的最右边是它自己，说明我要找的就是它，print 它，然后向右走。
class Solution3:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        stack = []
        curr = root
        while stack or curr:
            if curr.left:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                if pre.right != curr:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    result.append(curr.val)
                    curr = curr.right
            else:
                result.append(curr.val)
                curr = curr.right
        return result
