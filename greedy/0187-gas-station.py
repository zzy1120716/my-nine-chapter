"""
187. 加油站
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，
并且从第_i_个加油站前往第_i_+1个加油站需要消耗汽油cost[i]。
你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕
环路一周，一开始油箱为空。
求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案
，则返回-1。

样例
现在有4个加油站，汽油量gas[i]=[1, 1, 3, 1]，
环路旅行时消耗的汽油量cost[i]=[2, 2, 1, 1]。
则出发的加油站的编号为2。

挑战
O(n)时间和O(1)额外空间

注意事项
数据保证答案唯一。
"""
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        n = len(gas)
        diff = []
        for i in range(n):
            diff.append(gas[i] - cost[i])
        for i in range(n):
            diff.append(gas[i] - cost[i])
        if n == 1:
            if diff[0] >= 0:
                return 0
            else:
                return -1
        st = 0
        now = 1
        tot = diff[0]
        while st < n:
            while tot < 0:
                st = now
                now += 1
                tot = diff[st]
                if st > n:
                    return -1
            while now != st + n and tot >= 0:
                tot += diff[now]
                now += 1
            if now == st + n and tot >= 0:
                return st
        return -1