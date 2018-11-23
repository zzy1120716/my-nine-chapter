"""
196. Missing Number
给出一个包含 0 .. N 中 N 个数的序列，找出0 .. N 中没有出现在序列中的那个数。

样例
N = 4 且序列为 [0, 1, 3] 时，缺失的数为2。

挑战
在数组上原地完成，使用O(1)的额外空间和O(N)的时间。
"""


# 方法一：数学方法
# 等差数列求和公式，将全部数的和减去缺少一个数之后的和
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)


# 方法二：位运算
# 可以利用XOR是它自己的逆的事实在O(n)时间找到中缺少的元素。
# 因为我们知道nums包含n个数字并且在[0..n-1]范围内缺少一个数字，
# n肯定会替换nums中缺少的数字。因此，如果我们将一个整数初始化为n
# 并将其与每个索引和值进行异或，留下的将是缺少的数字。
# 示例：
# Index：0,1,2,3
# Value：0,1,3,4
# missing=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
# =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2=0∧0∧0∧0∧2=2
class Solution1:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# 方法三：HashSet
class Solution2:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        num_set = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in num_set:
                return num


# 方法四：排序
class Solution3:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)

        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num