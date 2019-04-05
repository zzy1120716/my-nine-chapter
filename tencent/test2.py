"""
示例：
输入：
3
8 5 10
1 1 2

输出：
2
"""


# 贪心，因为怪兽的贿赂价格只有1和2，分成四个情况
#
# 当前武力值超过目前这个怪兽，价格1，加入大顶队列
# 当前武力值少于目前怪兽，价格1，直接买
# 当前武力值少于，价格2，看看买堆顶怪兽行不行，行就买，不行就买现在这个
# 是当前武力值超过，价格2，不管他
if __name__ == "__main__":
    n = int(input())
    d = list(map(int, input().split()))
    p = list(map(int, input().split()))

    q = []

    ans = now = 0
    for i in range(n):
        if now < d[i] and p[i] == 1:
            ans += 1
            now += d[i]
        elif now >= d[i] and p[i] == 1:
            q.append(d[i])
        elif now < d[i] and p[i] == 2:
            if not q or now + q[0] < d[i]:
                ans += 2
                now += d[i]
            else:
                ans += 1
                now += q[0]
                q.pop()
    print(ans)
