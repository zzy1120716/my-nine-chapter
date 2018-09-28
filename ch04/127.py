"""
127. 拓扑排序
给定一个有向图，图节点的拓扑排序被定义为：
对于每条有向边A--> B，则A必须排在B之前　　
拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点　　
找到给定图的任一拓扑排序

样例
对于下列图：
这个图的拓扑排序可能是：
[0, 1, 2, 3, 4, 5]
或者
[0, 2, 3, 1, 5, 4]
或者
....

挑战
能否分别用BFS和DFS完成？

说明
Learn more about representation of graphs

注意事项
你可以假设图中至少存在一种拓扑排序
"""

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

{0,1,2,3,4#1,3,4#2,1,4#3,4#4}

graph = []
node0 = DirectedGraphNode(0)
node1 = DirectedGraphNode(1)
node2 = DirectedGraphNode(2)
node3 = DirectedGraphNode(3)
node4 = DirectedGraphNode(4)

node0.neighbors.extend([node1, node2, node3, node4])
graph.append(node0)

node1.neighbors.extend([node3, node4])
graph.append(node1)

node2.neighbors.extend([node1, node4])
graph.append(node2)

node3.neighbors.extend([node4])
graph.append(node3)

graph.append(node4)
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_to_indegree = self.get_indegree(graph)
        
        # bfs
        order = []
        # 得到所有入度为0的节点，作为起始节点
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        # 起始节点list保存为双端队列
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # return [node.label for node in order]
        return order
        
    
    # 构造 点->入度 dict
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        
        return node_to_indegree