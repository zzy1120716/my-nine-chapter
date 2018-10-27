"""
178. 图是否是树
给出 n 个节点，标号分别从 0 到 n - 1 并且给出一个 无向 边的列表 (给出每条边的两个顶点),
写一个函数去判断这张｀无向｀图是否是一棵树

样例
给出n = 5 并且 edges = [[0, 1], [0, 2], [0, 3], [1, 4]], 返回 true.

给出n = 5 并且 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], 返回 false.

注意事项
你可以假设我们不会给出重复的边在边的列表当中. 无向边　[0, 1] 和 [1, 0]　是同一条边，
因此他们不会同时出现在我们给你的边的列表当中。
"""

"""
方法一：
判断一个图是否为树：
1）n个节点的图有n-1条边
2）连通图
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # write your code here
        # 没有边，并且没有节点（空树），有一个节点（只有根节点的树）
        if (n == 0 or n == 1) and len(edges) == 0:
            return True
        if len(edges) != n - 1:
            return False

        # 构造邻接链表
        graph = {}
        for start, end in edges:
            if start not in graph:
                graph[start] = set([end])
            else:
                graph[start].add(end)
            if end not in graph:
                graph[end] = set([start])
            else:
                graph[end].add(start)

        queue = [edges[0][0]]
        visited = set()
        while queue:
            curr = queue.pop(0)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # 全部节点都被访问 --> 连通图
        return len(visited) == n


# 官方解法：使用defaultdict
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        from queue import Queue
        queue = Queue()

        queue.put(0)
        visited[0] = True
        while not queue.empty():
            cur = queue.get()
            visited[cur] = True
            for neighbor in neighbors[cur]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.put(neighbor)

        return len(visited) == n


"""
方法二：union find 并查集
"""
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False

        self.father = {i: i for i in range(n)}
        self.size = n

        for a, b in edges:
            self.union(a, b)

        return self.size == 1

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size -= 1
            self.father[root_a] = root_b

    def find(self, node):
        path = []
        while node != self.father[node]:
            path.append(node)
            node = self.father[node]

        for n in path:
            self.father[n] = node

        return node