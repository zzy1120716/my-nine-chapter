"""
570. 寻找丢失的数 II
给一个由 1 - n 的整数随机组成的一个字符串序列，其中丢失了一个整数，请找到它。

样例
给出 n = 20, str = 19201234567891011121314151618

丢失的数是 17 ，返回这个数。

注意事项
n <= 30
"""


# 官方答案DFS
class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        used = [False for _ in range(n + 1)]
        return self.dfs(n, str, 0, used)

    def dfs(self, n, str, index, used):
        if index == len(str):
            results = []
            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)
            return results[0] if len(results) == 1 else -1

        if str[index] == '0':
            return -1

        # length 1, 2
        for l in range(1, 3):
            num = int(str[index: index + l])
            # starts with 0 is invalid
            if 1 <= num <= n and not used[num]:
                used[num] = True
                target = self.dfs(n, str, index + l, used)
                if target != -1:
                    return target
                # backtracking
                used[num] = False

        return -1


# DFS模板，按照一个或者两个字母的方式切割字符串，然后在中间过程要尽可能的剪枝，否则会超时。
class Solution1:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        result = []
        self.dfs(n, str, [], result)
        sum = 0
        for p in result[0]:
            sum += int(p)
        # 通过求和找出丢失的数
        return n * (n + 1) // 2 - sum

    def dfs(self, n, str, path, result):
        if len(path) == n - 1 and str == "":
            result.append(path[:])
            return

        for i in range(1, 3):
            if i > len(str):
                break
            num = str[:i]
            if int(num) > n or int(num) < 0 or num in path:
                continue
            # 不能以0开始
            if i == 2 and num[0] == '0':
                continue
            path.append(num)
            self.dfs(n, str[i:], path, result)
            path.pop()


# 参考split string的方法，要判断找到的数字是否 valid，并且不能和已有的数字重复
# 最后返回一个正确的 partition，遍历一遍看哪个数不在就行了。注意这里的 partition
# 数组最好用 set，这样才能保证 O(1) 的 lookup time，或者像其他答案那样用一个 boolean
# 的 visited 标记也可以。
class Solution2:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, string):
        # write your code here
        if not string:
            return -1

        self.numbers = set()
        self.dfs(n, string, 0, set())

        # find the missing one
        for num in range(1, n + 1):
            if str(num) not in self.numbers:
                return int(num)

    def dfs(self, n, string, start_index, partition):
        if len(partition) == n - 1:
            self.numbers = set(partition)
            return

        for i in range(start_index, len(string)):
            substr = string[start_index: i + 1]
            if len(substr) > 2:
                break
            # check if the number represented by substring is valid
            if substr in partition or int(substr) > n or int(substr) < 1:
                continue  # not break

            self.dfs(n, string, i + 1, partition | set([substr]))


if __name__ == '__main__':
    s = Solution2()
    the_missing = s.findMissing2(20, '19201234567891011121314151618')
    print(the_missing)