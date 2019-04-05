"""
137. 克隆图
克隆一张无向图，图中的每个节点包含一个 label 和一个列表 neighbors。
保证每个节点的label均不同。

数据中如何表示一个无向图？http://www.lintcode.com/help/graph/

你的程序需要返回一个经过深度拷贝的新图。这个新图和原图具有同样的
结构，并且对新图的任何改动不会对原图造成任何影响。

样例
比如，序列化图 {0,1,2#1,2#2,2} 共有三个节点, 因此包含两个个分隔符#。

第一个节点label为0，存在边从节点0链接到节点1和节点2
第二个节点label为1，存在边从节点1连接到节点2
第三个节点label为2，存在边从节点2连接到节点2(本身),从而形成自环。
我们能看到如下的图：

   1
  / \
 /   \
0 --- 2
     / \
     \_/
"""
from collections import deque


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        root = node
        if node is None:
            return node
        
        # 使用 BFS 遍历图，并获得所有节点
        nodes = self.getNodes(node)
        
        # 复制节点，在hash中存储 旧->新 映射信息
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        # 复制 neighbors(edges)
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        
        return mapping[root]

    def getNodes(self, node):
        q = deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    q.append(neighbor)
        return result
