if __name__ == "__main__":
    n = int(input())
    s = input()
    zeros = s.count('0')
    ones = s.count('1')
    print(abs(zeros - ones))