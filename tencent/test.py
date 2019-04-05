if __name__ == "__main__":
    m, n = map(int, input().split())
    ans = 0
    amount = 0
    coins = []
    for i in range(n):
        coins.append(int(input()))
    coins.sort()
    if coins[0] == -1:
        print(0)
    while amount < m:
        for i in range(n - 1, -1, -1):
            if coins[i] <= amount + 1:
                amount += coins[i]
                ans += 1
                break
    print(ans)