"""
794. Sliding Puzzle II
On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the
initial state to final state.

If it is impossible to move from initial state to final state, return -1.

样例
Given an initial state:

[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
and a final state:

[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Return 4
Explanation:

[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]
挑战
How to optimize the memory?
Can you solve it with A* algorithm?
"""

"""
方法一：BFS
"""
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        source = self.matrix2str(init_state)
        target = self.matrix2str(final_state)

        from collections import deque
        queue = deque([source])
        visited = set([source])

        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == target:
                    return step

                # 遍历当前状态所有可能的下一状态
                for next in self.get_next(curr):
                    if next in visited:
                        continue
                    queue.append(next)
                    visited.add(next)
            step += 1

        return -1

    # 多维list转为字符串
    def matrix2str(self, state):
        res = ""
        for i in range(3):
            for j in range(3):
                res += str(state[i][j])
        return res

    # 获得下一步的所有可能
    def get_next(self, state):
        states = []
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        zero_idx = state.find('0')
        x = zero_idx // 3
        y = zero_idx % 3

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue

            state_list = list(state)
            # "0"与相邻位置元素互换位置
            state_list[x * 3 + y] = state_list[nx * 3 + ny]
            state_list[nx * 3 + ny] = '0'
            states.append("".join(state_list))

        return states


"""
方法二：A*算法
"""
# TODO
