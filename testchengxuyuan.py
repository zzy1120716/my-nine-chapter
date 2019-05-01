from sys import stdin


class Solution(object):

    def transform(self):
        mp = []
        while True:
            line = stdin.readline().strip()
            if line == '':
                break
            num = line.split(' ')
            num = [int(i) for i in num]
            mp.append(num)

        dp = [[0 for i in range(len(mp[0]) + 2)] for j in range(len(mp) + 2)]
        dp1 = [[0 for i in range(len(mp[0]) + 2)] for j in range(len(mp) + 2)]

        for i in range(1, len(dp) - 1):
            for j in range(1, len(dp[0]) - 1):
                dp[i][j] = mp[i - 1][j - 1]
        for i in range(1, len(dp) - 1):
            for j in range(1, len(dp[0]) - 1):
                dp1[i][j] = dp[i][j]
        if not self.isValid(dp):
            print(-1)
            return
        result = 0
        while not self.isValid1(dp):
            for i in range(1, len(dp) - 1):
                for j in range(1, len(dp[0]) - 1):
                    if dp[i][j] == 2:
                        dp1[i - 1][j] = 2
                        dp1[i + 1][j] = 2
                        dp1[i][j - 1] = 2
                        dp1[i][j + 1] = 2
            for i in range(1, len(dp) - 1):
                for j in range(1, len(dp[0]) - 1):
                    dp[i][j] = dp1[i][j]
            result += 1
        print(result)

    def isValid(self, dp):
        for i in range(1, len(dp) - 1):
            for j in range(1, len(dp[0]) - 1):
                if dp[i - 1][j] == 0 and dp[i + 1][j] == 0 and dp[i][j - 1] == 0 and dp[i][j + 1] == 0:
                    return False
        return True

    def isValid1(self, dp):
        for i in range(1, len(dp) - 1):
            for j in range(1, len(dp[0]) - 1):
                if dp[i][j] != 2:
                    return False
        return True


if __name__ == "__main__":
    '''
0 2
1 0
    '''
    s = Solution()
    s.transform()
