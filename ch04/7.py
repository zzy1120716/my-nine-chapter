"""

7. 二叉树的序列化和反序列化
设计一个算法，并编写代码来序列化和反序列化二叉树。将树
写入一个文件被称为“序列化”，读取文件后重建同样的二叉树
被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可
以将二叉树序列化为一个字符串，并且可以将字符串反序列化
为原来的树结构。

样例
给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如
下的树结构：

  3
 / \
9  20
  /  \
 15   7
我们的数据是进行BFS遍历得到的。当你测试结果wrong 
answer时，你可以作为输入调试你的代码。

你可以采用其他的方法进行序列化和反序列化。

注意事项
对二进制树进行反序列化或序列化的方式没有限制，LintCode
将您的serialize输出作为deserialize的输入，它不会检查序
列化的结果。
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

node1 = TreeNode(1)
node2 = TreeNode(2)
node1.right = node2
"""

"""
方法一：DFS
"""
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
        ans = []
        ans.append(str(root.val))
        ans.extend(self.serialize(root.left))
        ans.extend(self.serialize(root.right))
        return ans

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        ch = data.pop(0)
        if ch == '#':
            return None
        else:
            root = TreeNode(int(ch))
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root


"""
方法二：BFS
"""
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ['#']
        queue = collections.deque([root])
        ans = []
        while queue:
            node = queue.popleft()
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('#')
        return ans
        

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data[0] == '#':
            return None
        root = TreeNode(int(data.pop(0)))
        queue = collections.deque([root])
        # flag用来区分当前节点是左还是右
        isLeft = True
        while data:
            ch = data.pop(0)
            if ch != '#':
                node = TreeNode(int(ch))
                queue.append(node)
                if isLeft:
                    queue[0].left = node
                else:
                    queue[0].right = node
            # 处理完右子节点，可以出队
            if not isLeft:
                queue.popleft()
            isLeft = not isLeft
        return root