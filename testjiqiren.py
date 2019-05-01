if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split()))

    '''
5
3 4 3 2 4
    '''
    e = h[n - 1]
    for i in range(n - 2, -1, -1):
        e = h[i] + e
        e /= 2
        if e > int(e):
            e = int(e) + 1.0
    print(int(e))