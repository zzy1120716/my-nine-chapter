"""
362. 滑动窗口的最大值
中文English
给出一个可能包含重复的整数数组，和一个大小为 k 的滑动窗口,
从左到右在数组中滑动这个窗口，找到数组中每个窗口内的最大值。

样例
给出数组 [1,2,7,7,8], 滑动窗口大小为 k = 3. 返回 [7,7,8].

解释：

最开始，窗口的状态如下：

[|1, 2 ,7| ,7 , 8], 最大值为 7;

然后窗口向右移动一位：

[1, |2, 7, 7|, 8], 最大值为 7;

最后窗口再向右移动一位：

[1, 2, |7, 7, 8|], 最大值为 8.

挑战
O(n)时间，O(k)的额外空间
"""
from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums:
            return []
        res = []
        stack = deque()
        for i in range(k):
            self.push(nums, stack, i)

        res.append(nums[stack[0]])
        for i in range(k, len(nums)):
            if stack[0] <= i - k:
                stack.popleft()
            self.push(nums, stack, i)
            res.append(nums[stack[0]])

        return res

    def push(self, nums, stack, i):
        while stack and nums[i] > nums[stack[-1]]:
            stack.pop()
        stack.append(i)


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1, 2, 7, 7, 8], 3))

