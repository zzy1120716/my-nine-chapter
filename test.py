if __name__ == '__main__':
    s = input()
    n = len(s)
    if not s:
        print(0)
    max_len = 1
    for i in range(1, n - 1):
        left, right = i - 1, i + 1
        while left >= 0:
            if s[left] != s[left + 1]:
                left -= 1
            else:
                break
        while right < n:
            if s[right] != s[right - 1]:
                right += 1
            else:
                break
        max_len = max(max_len, right - left - 1)
    print(max_len)