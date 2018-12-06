"""
945. Task Scheduler
Given a char array representing tasks CPU need to do. 
It contains capital letters A to Z where different letters 
represent different tasks.Tasks could be done without original 
order. Each task could be done in one interval. For each interval, 
CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means 
between two same tasks, there must be at least n intervals that 
CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will 
take to finish all the given tasks.

样例
Given tasks = ['A','A','A','B','B','B'], n = 2, return 8.
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B.

注意事项
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        # ['A','A','A','B','B','B'], n = 2, return 8.
        # A -> B -> idle -> A -> B -> idle -> A -> B.
        c = [0 for _ in range(26)]
        for t in tasks:
            c[ord(t) - ord('A')] += 1
        c.sort()
        i = 25
        while i >= 0 and c[i] == c[25]:
            i -= 1
        
        return max(len(tasks), (c[25] - 1) * (n + 1) + 25 - i)