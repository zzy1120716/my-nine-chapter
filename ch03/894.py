"""
class FlipTool:

    @classmethod
    def flip(cls, arr, i):
        ...
"""
class Solution:
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