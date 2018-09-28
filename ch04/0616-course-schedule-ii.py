"""
616. 安排课程
你需要去上n门九章的课才能获得offer，这些课被标号为 0 到 n-1 。
有一些课程需要“前置课程”，比如如果你要上课程0，
你需要先学课程1，我们用一个匹配来表示他们： [0,1]

给你课程的总数量和一些前置课程的需求，返回你为了学完
所有课程所安排的学习顺序。

可能会有多个正确的顺序，你只要返回一种就可以了。如果
不可能完成所有课程，返回一个空数组。

样例
给定 n = 2, prerequisites = [[1,0]]
返回 [0,1]

给定 n = 4, prerequisites = [1,0],[2,0],[3,1],[3,2]]
返回 [0,1,2,3] or [0,2,1,3]
"""
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]

        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        from queue import Queue
        q = Queue(maxsize = numCourses)
        
        for i in range(numCourses):
            if degrees[i] == 0:
                q.put(i)
                
        order =[]
        while not q.empty():
            node = q.get()
            order.append(node)
            
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    q.put(x)
                    
        if len(order) == numCourses:
            return order
        
        return []