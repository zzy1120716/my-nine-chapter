"""
示例：
输入：
3
8 5 10
1 1 2

输出：
2
"""


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
