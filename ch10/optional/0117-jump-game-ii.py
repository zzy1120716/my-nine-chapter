"""
117. 跳跃游戏 II
给出一个非负整数数组，你最初定位在数组的第一个位置。
数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

样例
给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2
(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)
"""


# 方法一：动态规划，会超时，但必须掌握O(n^2)
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        # state
        steps = [float('inf')] * (len(A))

        # initialize
        steps[0] = 0

        # function
        for i in range(1, len(A)):
            for j in range(i):
                if steps[j] != float('inf') and j + A[j] >= i:
                    steps[i] = min(steps[i], steps[j] + 1)

        # answer
        return steps[len(A) - 1]


# 方法二：Greedy 最大化每次跳跃的长度
class Solution1:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        current_index = 0
        target_index = len(A) - 1
        total_jumps = 0

        while current_index < target_index:
            total_jumps += 1
            jump_range = range(current_index, current_index + A[current_index] + 1)
            if target_index in jump_range:
                break

            next_index = current_index
            for next_index_candidate in jump_range:
                candidate_jump_destination = next_index_candidate + A[next_index_candidate]
                next_jump_destination = next_index + A[next_index]
                if next_jump_destination < candidate_jump_destination:
                    next_index = next_index_candidate

            current_index = next_index

        return total_jumps


# 方法三：BFS
class Solution2:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if len(A) <= 1:
            return 0
        # 标记每一层的最后一个元素
        cur_max = 0
        level = i = 0
        while i <= cur_max:
            # 标记下一层的最后一个元素
            furthest = cur_max
            for i in range(cur_max + 1):
                furthest = max(furthest, A[i] + i)
                if furthest >= len(A) - 1:
                    return level + 1
            level += 1
            cur_max = furthest
        # 如果 i < cur_max，i不能再向前移动（list中的最后一个元素无法到达）
        return -1


# 方法四：贪心法，获取每一次跳跃的最大跳跃长度
class Solution3:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        if len(A) == 1:
            return 0
        if A[0] > len(A) - 1:
            return 1
        max_jump, end, num_jump = A[0], A[0], 1

        i = 1
        while max_jump < len(A) - 1:
            if i <= end:
                # get max jump at the next time
                max_jump = max(max_jump, A[i] + i)
                i += 1
                continue
            num_jump += 1
            end = max_jump
        return num_jump + 1
