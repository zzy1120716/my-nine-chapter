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