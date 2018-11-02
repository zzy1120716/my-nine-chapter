"""
426. 恢复IP地址
给一个由数字组成的字符串。求出其可能恢复为的所有IP地址。

样例
给出字符串 "25525511135"，所有可能的IP地址为：

[
  "255.255.11.135",
  "255.255.111.35"
]
（顺序无关紧要）
"""


# DFS套用九章算法班模板
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, path, results):
        if len(path) == 4 and s == "":
            results.append(".".join(path[:]))
            return
        for i in range(1, 4):
            if i > len(s):
                break
            num = s[:i]
            # 跳过大于255的字符串
            if int(num) > 255:
                continue
            # 跳过以“00”开头的字符串
            if len(num) >= 2 and num[0] == '0' and num[0] == '0':
                continue
            path.append(num)
            self.dfs(s[i:], path, results)
            path.pop()


# 官方答案
class Solution1:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        ips = []
        self.dfs(s, 0, ips, '')
        return ips

    def dfs(self, s, sub, ips, ip):
        # should be 4 parts
        if sub == 4:
            if s == '':
                # remove first '.'
                ips.append(ip[1:])
            return
        for i in range(1, 4):
            # the three ifs' order cannot be changed!
            # if i > len(s), s[:i] will make false!!!!
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                # make sure that result just can be '0.0.0.0' and remove like '00'
                if s[0] == '0':
                    break


# 类似split string的解法
class Solution2:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(s, results, 0, [])
        return results

    def dfs(self, s, results, start_index, subset):
        if len(subset) == 4 and start_index == len(s):
            results.append('.'.join(subset))
            return

        for i in range(start_index, start_index + 3):
            if i >= len(s):
                return
            substring = s[start_index: i + 1]
            num = int(substring)
            if num < 0 or num > 255 or len(substring) != len(str(num)):
                continue
            subset.append(substring)
            self.dfs(s, results, i + 1, subset)
            subset.pop()


if __name__ == '__main__':
    s = Solution()
    results = s.restoreIpAddresses("25525511135")
    print(results)