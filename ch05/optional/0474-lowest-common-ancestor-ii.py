"""
474. 最近公共祖先 II
给一棵二叉树和二叉树中的两个节点，找到这两个节点的最近公共祖先LCA。

两个节点的最近公共祖先，是指两个节点的所有父亲节点中（包括这两个节点），
离这两个节点最近的公共的节点。

每个节点除了左右儿子指针以外，还包含一个父亲指针parent，指向自己的父亲。

样例
对于下面的这棵二叉树

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
"""

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

"""
1）由于每个节点都有一个指向其父节点的指针，因此，从节点A开始向上遍历，
将沿途所有A的祖先节点（父节点，祖父节点……）都保存到set中；
2）从节点B开始向上遍历，遇到的祖先节点如果已经在set中存在，则必然是A和B
的最近公共祖先节点，直接返回
"""


class Solution:

    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        parent_set = set()

        curr = A
        while curr:
            parent_set.add(curr)
            curr = curr.parent

        curr = B
        while curr:
            if curr in parent_set:
                return curr
            curr = curr.parent

        return None


class Solution1:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        p1, p2 = A, B
        while p1 != p2:
            p1 = B if not p1.parent else p1.parent
            p2 = A if not p2.parent else p2.parent
        return p1


# 官方答案，辅助函数找到A和B分别到root的path，随后从后向前比较两个list即可
class Solution2:
    
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        path_a = self.get_path2root(A)
        path_b = self.get_path2root(B)

        index_a = len(path_a) - 1
        index_b = len(path_b) - 1

        # lowest common ancestor
        lca = None
        while index_a >= 0 and index_b >= 0:
            if path_a[index_a] != path_b[index_b]:
                break
            lca = path_a[index_a]
            index_a -= 1
            index_b -= 1

        return lca

    def get_path2root(self, node):
        path = []
        while node:
            path.append(node)
            node = node.parent
        return path
