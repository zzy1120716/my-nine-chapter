"""
531. 六度问题
六度分离是一个哲学问题，说的是每个人每个东西可以通过六步或者更少的步数建立联系。

现在给你一个友谊关系，查询两个人可以通过几步相连，如果不相连返回 -1

样例
给出图

1------2-----4
 \          /
  \        /
   \--3--/
{1,2,3#2,1,4#3,1,4#4,2,3} s = 1, t = 4 返回 2

给出图二


1      2-----4
             /
           /
          3
{1#2,4#3,4#4,2,3} s = 1, t = 4 返回 -1
"""

"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):
        # write your code here
        if s == t or not graph:
            return 0

        queue = [s]
        dist = {}
        dist[s] = 0

        while queue:
            curr = queue.pop(0)
            if curr == t:
                return dist[curr]
            for neighbor in curr.neighbors:
                if neighbor not in dist:
                    dist[neighbor] = dist[curr] + 1
                    queue.append(neighbor)

        return -1