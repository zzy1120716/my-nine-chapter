if __name__ == '__main__':
    from collections import Counter
    n = int(input().strip())
    b = list(map(int, input().strip().split(' ')))
    # print(n, b)
    d = Counter(b)
    a = [v for _, v in d.items()]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    res = a[0]
    for c in a[1::]:
        res = gcd(res, c)

    ans = 0
    for num in a:
        ans += num // res
    if res < 2:
        print(0)
    else:
        print(ans)