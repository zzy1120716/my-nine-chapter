"""
894. Pancake Sorting
Given an an unsorted array, sort the given array. You are allowed to do only following
operation on array.

flip(arr, i): Reverse array from 0 to i
Unlike a traditional sorting algorithm, which attempts to sort with the fewest
comparisons possible, the goal is to sort the sequence in as few reversals as possible.

样例
Given array = [6, 7, 10, 11, 12, 20, 23]
Use flip(arr, i) function to sort the array.

注意事项
You only call flip function.
Don't allow to use any sort function or other sort methods.

Java：you can call FlipTool.flip(arr, i)
C++： you can call FlipTool::flip(arr, i)
Python2&3 you can call FlipTool.flip(arr, i)
"""


class FlipTool:
    @classmethod
    def flip(cls, arr, i):
        j = 0
        while j < i:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
            i -= 1


# 因为每次翻转必会动a[0]，所以sorting要从最末位开始
# 每一轮将范围内最大值翻转至a[0]，然后再翻转0-目标位置，将最大值放到目标位置
# 时间复杂度：O(n^2)，空间复杂度：O(1)
class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        for i in range(len(array) - 1, 0, -1):
            max_idx = 0
            for j in range(i + 1):
                if array[j] > array[max_idx]:
                    max_idx = j
            FlipTool.flip(array, max_idx)
            FlipTool.flip(array, i)


class Solution1:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        for i in range(len(array) - 1, 0, -1):
            mi = self.findMax(array, i)
            FlipTool.flip(array, mi)
            FlipTool.flip(array, i)

    def findMax(self, array, n):
        mi = 0
        for i in range(n + 1):
            if array[i] > array[mi]:
                mi = i
        return mi


if __name__ == '__main__':
    array = [6, 11, 10, 12, 7, 23, 20]
    Solution().pancakeSort(array)
    print(array)
