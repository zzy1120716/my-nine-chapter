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
    visited = [0] * n
    su = 0
    tmp = float('inf')
    flag = 0
    i = 1
    while i < n:
        j = 1
        tmp = 10000
        while j < n:
            k = 0
            flag = 0
            while k < i:
                if visited[k] == j:
                    flag = 1
                    break
                else:
                    k += 1
            if flag == 0 and m[j][visited[i - 1]] < tmp:
                l = j
                tmp = m[j][visited[i - 1]]
            j += 1
        visited[i] = l
        i += 1
        su += tmp
    su += m[0][l]
    print(su)