"""
58. 四数之和
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

样例
例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：

(-1, 0, 0, 1)

(-2, -1, 1, 2)

(-2, 0, 0, 2)

注意事项
四元组(a, b, c, d)中，需要满足a <= b <= c <= d

答案中不可以包含重复的四元组。
"""


# 方法一：多枚举一个数后，参照3Sum的做法，O(N^3)
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        # write your code here
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res


# 方法二：DFS
# 核心是实现一个快速的2指针方法来解决2-sum，以及递归以将N-sum减少到2-sum。
class Solution1:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i - 1] != nums[i]):
                        findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums) - 1, target, 4, [], results)
        return results


# 方法二的另一种形式
class Solution2:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
        return


if __name__ == '__main__':
    print(Solution2().fourSum([1, 0, -1, 0, -2, 2], 0))