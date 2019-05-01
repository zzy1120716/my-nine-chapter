class Solution:

    def __init__(self):
        self.min_len = float('inf')

    def exist(self, d, init, target):
        if not d:
            return -1
        self.dfs(d, [init], init, target)

    def dfs(self, d, visited, n, target):
        if n == target:
            self.min_len = min(len(visited), self.min_len)
            return
        for i in list(d[n]):
            if i not in visited:
                visited.append(i)
                self.dfs(d, visited, i, target)
                visited.pop()


if __name__ == '__main__':
    import sys

    ssn = []
    while True:
        sn = sys.stdin.readline().strip()
        if sn == '':
            break
        sn = list(sn.split(','))
        ssn.append(sn)

    init, target = ssn[0][0], ssn[0][1]

    d = {}
    for end, start in ssn[1:]:
        if start != 'NULL':
            if start not in d:
                d[start] = set()
            d[start].add(end)

    Solution().exist(d, init, target)
    print(Solution().min_len)

'''
A,F
A,NULL
B,A
D,B
F,B
E,A
F,E
E,D
D,B
C,B
B,G
G,F
C,F
'''