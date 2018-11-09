"""
548. 两数组的交集 II
给定两个数组，计算两个数组的交集

样例
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

挑战
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to num2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
注意事项
每个元素出现次数得和在数组里一样
答案可以以任意顺序给出
"""


# 方法一：利用Counter
import collections


class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        counts = collections.Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


# 方法二：利用hash
class Solution1:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        h = {}
        for i in range(len(nums1)):
            if nums1[i] in h:
                h[nums1[i]] += 1
            else:
                h[nums1[i]] = 1

        result = []

        for i in range(len(nums2)):
            if nums2[i] in h and h[nums2[i]] > 0:
                result.append(nums2[i])
                h[nums2[i]] -= 1

        return result


# 方法三：先排序，再向后扫描，遇到相同的就丢到结果list中
class Solution2:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        return result


if __name__ == '__main__':
    print(Solution2().intersection([1, 2, 2, 1], [2, 2]))