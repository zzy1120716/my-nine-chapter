"""
460. 在排序数组中找最接近的K个数
给一个目标数 target, 一个非负整数 k, 一个按照升序排列
的数组 A。在A中找与target最接近的k个整数。返回这k个数
并按照与target的接近程度从小到大排序，如果接近程度相当，
那么小的数排在前面。

样例
如果 A = [1, 2, 3], target = 2 and k = 3, 那么返回
[2, 1, 3].

如果 A = [1, 4, 6, 8], target = 3 and k = 3, 那么返回
[4, 1, 6].

挑战
O(logn + k) 的时间复杂度

注意事项
1.k是一个非负整数，并且总是小于已排序数组的长度。
2.给定数组的长度是有意义的,不会超过10 ^ 4
3.组中元素的绝对值不会超过10 ^ 4
"""
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if k <= 0 or A is None or len(A) == 0:
            return []
        
        result = []
        
        left = self.binarySearch(A, target)
        right = left + 1
        
        for i in range(k):
            if self.isLeftCloser(A, target, left, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        
        return result
            
    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        
        if right >= len(A):
            return True
            
        if target - A[left] != A[right] - target:
            return target - A[left] < A[right] - target
        
        return True

    def binarySearch(self, A, target):
        
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if A[mid] < target:
                start = mid
            else:
                end = mid
                
        if target - A[start] <= A[end] - target:
            return start
        else:
            return end