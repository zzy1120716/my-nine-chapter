"""
379. 将数组重新排序以构造最小值
中文English
给定一个整数数组，请将其重新排序，以构造最小值。

样例
样例 1：

输入：[2, 1]
输出：[1, 2]
解释：通过将数组重新排序，可构造 2 个可能性数字：
           1+2=12
           2+1=21
其中，最小值为 12，所以，将数组重新排序后，该数组变为 [1, 2]。
样例 2：

输入：[3, 32, 321]
输出：[321, 32, 3]
解释：通过将数组重新排序，可构造 6 个可能性数字：
3+32+321=332321
3+321+32=332132
32+3+321=323321
32+321+3=323213
321+3+32=321332
321+32+3=321323
其中，最小值为 321323，所以，将数组重新排序后，该数组变为 [321, 32, 3]。
挑战
在原数组上完成，不使用额外空间。

注意事项
The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key


# 方法一：
class Solution:
    """
    @param nums: n non-negative integer array
    @return: A string
    """
    def minNumber(self, nums):
        # write your code here
        if not nums:
            return ''

        strings = [str(num) for num in nums]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if strings[i] + strings[j] > strings[j] + strings[i]:
                    strings[i], strings[j] = strings[j], strings[i]

        return str(int(''.join(strings)))


# 方法二：
class Solution2:
    """
    @param nums: n non-negative integer array
    @return: A string
    """
    def minNumber(self, nums):
        # write your code here

        nums.sort(key=cmp_to_key(lambda a, b: int(str(a) + str(b)) - int(str(b) + str(a))))

        result = ''.join([str(ele) for ele in nums])
        i, length = 0, len(result)
        while i + 1 < length:
            if result[i] != '0':
                break
            i += 1

        return result[i:]

    def cmp(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return -1
        elif str(a) + str(b) == str(b) + str(a):
            return 1
        else:
            return 0


if __name__ == '__main__':
    # 321323
    print(Solution2().minNumber([3, 32, 321]))
