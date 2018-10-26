"""
618. 搜索图中节点
给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点最近 且 值为目标值的节点，
如果不能找到则返回 NULL。
在给出的参数中, 我们用 map 来存节点的值

样例
2------3  5
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      1 --4
给出 节点1，目标值为 50

有个哈希表的值为[3,4,10,50,50]，表示:
节点1的值为3
节点2的值为4
节点3的值为10
节点4的值为50
节点5的值为50

返回 节点4
注意事项
保证答案唯一
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# 直接在values上修改
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        # 起点的值直接等于目标值
        if values[node] == target:
            return node

        from collections import deque
        queue = deque([node])
        # 访问后直接把map中的节点删除
        del values[node]

        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor in values:
                    if values[neighbor] == target:
                        return neighbor
                    del values[neighbor]
                    queue.append(neighbor)

        return None

# 常规方法，visited集合记录访问过的节点
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        q = [node]
        visited = set([node])
        while q:
            head = q.pop(0)
            if values[head] == target:
                return head
            for neighbor in head.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return None
