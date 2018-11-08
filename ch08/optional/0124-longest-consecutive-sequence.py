"""
124. 最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

样例
给出数组[100, 4, 200, 1, 3, 2]，这个最长的连续序列是 [1, 2, 3, 4]，返回所求长度 4

说明
要求你的算法复杂度为O(n)
"""


# 方法一：暴力法（超时）
# 每取出一个数，就检查比这个数大1的数是否在数组中
# 时间复杂度O(n ^ 3)，空间O(1)
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


# 方法二：排序
# 判断后一个数是否是前一个数 + 1
# 一个值存储当前最大连续长度，与全局最大连续长度打擂台
# 时间复杂度O(nlogn)，
# 空间O(1)（允许给传入数组自身排序）或O(n)（不允许原地排序）
class Solution1:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


# 方法三：Set和智能序列构建
# 时间和空间复杂度都是O(n)
class Solution2:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # current number is a lower bound
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # check if there any large and consecutive number exists
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# 方法四：哈希表方法
# 分三种情况讨论：
# 1. 没邻居 h[key] = 1
# 2. 只有一个邻居，则将value拓展，L = h[key + 1] = h[key - 1]
# h[key + 1] = h[key - 1] = h[key] = L + 1
# 3. 有两个邻居，是连接两部分序列的bridge
# L = h[key - 1], R = h[key + 1], T = L + R + 1
# h[key - L] = h[key + R] = T
class Solution3:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        # hash_table
        h = {}
        for num in nums:
            if num in h:
                continue

            l = h.get(num - 1, 0)
            r = h.get(num + 1, 0)

            # bridge
            if l > 0 and r > 0:
                h[num] = h[num - l] = h[num + r] = l + r + 1
            # one neighbor
            elif l > 0:
                h[num] = h[num - l] = l + 1
            elif r > 0:
                h[num] = h[num + r] = r + 1
            # no neighbor
            else:
                h[num] = 1

        # get largest value in hash table as longest streak
        longest_streak = 0
        for key, val in h.items():
            longest_streak = max(longest_streak, val)

        return longest_streak


# 方法四改进版：不单独考虑是否有左右邻居，直接都置为T
# 在线（online）方式取得最大值（打擂台）
class Solution4:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, nums):
        # write your code here
        # hash table
        h = {}
        longest_streak = 0

        for num in nums:
            if num in h:
                continue

            l = h.get(num - 1, 0)
            r = h.get(num + 1, 0)
            t = l + r + 1

            h[num] = h[num - l] = h[num + r] = t

            longest_streak = max(longest_streak, t)

        return longest_streak


if __name__ == '__main__':
    ans = Solution4().longestConsecutive([100, 4, 200, 1, 3, 2])
    print(ans)
