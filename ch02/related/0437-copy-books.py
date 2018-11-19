"""
437. 书籍复印
给出一个数组A包含n个元素，表示n本书以及各自的页数。现在有个k个人复印书籍，每个人只能复印连续一段编号的书，
比如A[1],A[2]由第一个人复印，但是不能A[1],A[3]由第一个人复印，求最少需要的时间复印所有书。

样例
A = [3,2,4],k = 2

返回5，第一个人复印前两本书
"""


# 方法一：基于答案值域的二分法
# 答案的范围在 max(pages)~sum(pages) 之间，每次二分到一个时间 time_limit 的时候，
# 用贪心法从左到右扫描一下 pages，看看需要多少个人来完成抄袭。
# 如果这个值 <= k，那么意味着大家花的时间可能可以再少一些，如果 > k 则意味着人数不够，
# 需要降低工作量。
# 时间复杂度 O(nlog(sum))是该问题时间复杂度上的最优解法。
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_least_people(pages, start) <= k:
            return start
        return end

    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page

        return count + 1


# 方法二：动态规划
class Solution1:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        n = len(pages)
        if k > n:
            k = n

        if n == 0:
            return 0

        sum = [0] * n
        sum[0] = pages[0]
        for i in range(1, n):
            sum[i] = sum[i - 1] + pages[i]

        f = [[0] * k for _ in range(n)]

        for i in range(n):
            f[i][0] = sum[i]

        for j in range(1, k):
            p = 0
            f[0][j] = pages[0]
            for i in range(1, j):
                f[i][j] = max(f[i - 1][j], pages[i])

            for i in range(j, n):
                while p < i and f[p][j - 1] < sum[i] - sum[p]:
                    p += 1
                f[i][j] = max(f[p][j - 1], sum[i] - sum[p])
                if p > 0:
                    p -= 1
                f[i][j] = min(f[i][j], max(f[p][j - 1], sum[i] - sum[p]))

        return f[n - 1][k - 1]


if __name__ == '__main__':
    print(Solution().copyBooks([3, 2, 4], 2))
    # 9982
    print(Solution().copyBooks(
        [393, 8306, 2935, 9673, 3769, 9181, 4804, 199, 5305, 9089, 3522, 9676, 6083, 5340, 3634, 55, 2298, 497, 4892,
         977, 5026, 3253, 8548, 60, 4016, 6299, 6812, 7005, 7047, 6647, 1961, 8846, 2064, 8800, 4873, 1515, 5526, 1771,
         8045, 1906, 2015, 8154, 1107, 4042, 1549, 9553, 7278, 2290, 2378, 3884, 6901, 6337, 9797, 5583, 1435, 2064,
         757, 2313, 4825, 2102, 5160, 3916, 4558, 7694, 2851, 7149, 8104, 9531, 2943, 3490, 5390, 6865, 122, 2511, 3567,
         7822, 897, 9675, 7369, 6949, 1923, 6926, 7869, 2205, 961, 2313, 9166, 5848, 1568, 8898, 4921, 9982, 9025, 529,
         1235, 405, 8847, 3816, 156, 2416], 10001))
