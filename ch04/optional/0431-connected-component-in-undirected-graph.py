"""
431. 找无向图的连通块
找出无向图中所有的连通块。

图中的每个节点包含一个label属性和一个邻接点的列表。（一个无向图的连通块是一个子图，
其中任意两个顶点通过路径相连，且不与整个图中的其它顶点相连。）

样例
给定图:

A------B  C
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      D   E
返回 {A,B,D}, {C,E}。其中有 2 个连通块，即{A,B,D}, {C,E}

说明
Learn more about representation of graphs

注意事项
每个连通块内部应该按照label属性排序
"""

"""
方法一：BFS
记录访问过的节点
对每个节点做一次bfs，做一次就在结果中增加一个子图序列
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        result = []
        visited = set()

        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))
        return result

    def bfs(self, node, visited, subgraph):
        queue = [node]
        visited.add(node)
        while queue:
            curr = queue.pop(0)
            subgraph.append(curr.label)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


"""
方法二：DFS
"""
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        self.visited = {}
        for node in nodes:
            self.visited[node.label] = False

        result = []
        for node in nodes:
            if not self.visited[node.label]:
                tmp = []
                self.dfs(node, tmp)
                result.append(sorted(tmp))
        return result

    def dfs(self, node, tmp):
        self.visited[node.label] = True
        tmp.append(node.label)
        for neighbor in node.neighbors:
            if not self.visited[neighbor.label]:
                self.dfs(neighbor, tmp)


"""
方法三：Union Find
"""
class Solution:

    def __init__(self):
        self.d = {}

    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        for node in nodes:
            self.d[node.label] = None
        for node in nodes:
            for neighbor in node.neighbors:
                a = self.find_parent(node.label)
                b = self.find_parent(neighbor.label)
                if a != b:
                    self.d[a] = b
        result = {}
        for k in self.d:
            key = self.find_parent(k)
            result[key] = result.get(key, []) + [k]
        return sorted([sorted(i) for i in result.values()])

    def find_parent(self, n):
        if self.d[n]:
            return self.find_parent(self.d[n])
        return n