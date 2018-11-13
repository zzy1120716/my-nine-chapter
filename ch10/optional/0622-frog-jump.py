"""
622. 青蛙跳
一只青蛙正要过河，这条河分成了 x 个单位，每个单位可能存在石头，
青蛙可以跳到石头上，但它不能跳进水里。
按照顺序给出石头所在的位置，判断青蛙能否到达最后一块石头所在的位置。
刚开始时青蛙在第一块石头上，假设青蛙第一次跳只能跳一个单位的长度。
如果青蛙最后一个跳 k 个单位，那么它下一次只能跳 k - 1 ，k 或者 k + 1 个单位。
注意青蛙只能向前跳。

样例
给出石头的位置为 [0,1,3,5,6,8,12,17]

总共8块石头。
第一块石头在 0 位置，第二块石头在 1 位置，第三块石头在 3 位置等等......
最后一块石头在 17 位置。

返回 true。青蛙可以通过跳 1 格到第二块石头，跳 2 格到第三块石头，跳 2 格到第四块石头，
跳 3 格到第六块石头，跳 4 格到第七块石头，最后跳 5 格到第八块石头。

给出石头的位置为 `[0,1,2,3,4,8,9,11]`
返回 false。青蛙没有办法跳到最后一块石头因为第五块石头跟第六块石头的距离太大了。
注意事项
石头的个数 >= 2并且 <= 1100。
每块石头的位置是一个非负数并且 < 2^31。
第一块石头的位置总是 0.
"""


# 方法一：hash记录石头上一次来源
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        if not stones:
            return False
        # hash存储每块石头的来源，上一步跳的距离，即last step
        h = {}
        for i in range(len(stones)):
            h[stones[i]] = set()
        # 注意初始化设定0这块石头，默认last step为0
        h[0].add(0)

        for i in range(len(stones)):
            for last_step in h[stones[i]]:
                # next_step 可以取的步数为 last_step - 1, last_step, last_step + 1
                for next_step in range(last_step - 1, last_step + 2):
                    # 是向前跳，并且能跳到下个石头上，就记录下来
                    if next_step > 0 and (stones[i] + next_step) in h:
                        h[stones[i] + next_step].add(next_step)

        return True if h[stones[-1]] else False


# 官方答案
class Solution1:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        dp = {}
        for stone in stones:
            dp[stone] = set([])
        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                # k - 1
                if k - 1 > 0 and stone + k - 1 in dp:
                    dp[stone + k - 1].add(k - 1)
                # k
                if stone + k in dp:
                    dp[stone + k].add(k)
                # k + 1
                if stone + k + 1 in dp:
                    dp[stone + k + 1].add(k + 1)

        return len(dp[stones[-1]]) > 0


# 方法二：BFS，加一个二维哈希做去重，避免访问相同节点
class Solution2:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here
        if not stones:
            return False

        s = set(stones)

        queue = [(stones[0], 0)]
        visited = {(stones[0], 0): True}

        for pos, k in queue:
            if pos == stones[-1]:
                return True
            for x in (k - 1, k, k + 1):
                if x > 0 and not visited.get((pos + x, x)) and pos + x in s:
                    visited[pos + x, x] = True
                    queue.append((pos + x, x))

        return False


if __name__ == '__main__':
    print(Solution2().canCross([0, 1, 3, 5, 6, 8, 12, 17]))
