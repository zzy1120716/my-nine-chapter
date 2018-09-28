class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        edges = {i : [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]
        
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        
        from queue import Queue
        q, count = Queue(maxsize = numCourses), 0
        
        for i in range(numCourses):
            if degrees[i] == 0:
                q.put(i)
                
        while not q.empty():
            node = q.get()
            count += 1
            
            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    q.put(x)
        
        return count == numCourses