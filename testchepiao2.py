class Solution:

    def __init__(self, X, start_node):
        self.X = X  # 距离矩阵
        self.start_node = start_node  # 开始的节点
        self.array = [[0] * (2 ** len(self.X)) for i in range(len(self.X))]  # 记录处于x节点，未经历M个节点时，矩阵储存x的下一步是M中哪个节点

    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2 ** s  # 二进制转换
        return su

    # tsp总接口
    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = [i for i in range(num)]
        #cities = range(num)  # 形成节点的集合
        past_sets = [s]  # 已遍历节点集合
        cities.pop(cities.index(s))  # 构建未经历节点的集合
        node = s  # 初始节点
        return self.solve(node, cities)  # 求解函数

    def solve(self, node, future_sets):
        # 迭代终止条件，表示没有了未遍历节点，直接连接当前节点和起点即可
        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        # d = 99999
        d = float('inf')
        # node如果经过future_sets中节点，最后回到原点的距离
        distance = []
        # 遍历未经历的节点
        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i)  # 删除第i个节点，认为已经完成对其的访问
            distance.append(self.X[node][s_i] + self.solve(s_i, copy))
        # 动态规划递推方程，利用递归
        d = min(distance)
        # node需要连接的下一个节点
        next_one = future_sets[distance.index(d)]
        # 未遍历节点集合
        c = self.transfer(future_sets)
        # 回溯矩阵，（当前节点，未遍历节点集合）——>下一个节点
        self.array[node][c] = next_one
        return d


if __name__ == '__main__':

    '''
4
0 2 6 5
2 0 4 4
6 4 0 2
5 4 2 0
    '''

    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))
    # D = [[-1,10,20,30,40,50],[12,-1,18,30,25,21],[23,19,-1,5,10,15],[34,32,4,-1,8,16],[45,27,11,10,-1,18],[56,22,16,20,12,-1]]
    S = Solution(m, 0)
    print(S.tsp())
