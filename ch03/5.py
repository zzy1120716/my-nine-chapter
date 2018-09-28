class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or len(A) == 0:
            return -1
            
        return self.quickSelect(A, 0, len(A) - 1, k)
        
    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]
            
        i, j = start, end
        pivot = A[(start + end) // 2]
        
        while i <= j:
            while i <= j and A[i] > pivot:
                i += 1
            
            while i <= j and A[j] < pivot:
                j -= 1
                
            if i <= j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
                
        if start + k - 1 <= j:
            return self.quickSelect(A, start, j, k)
            
        if start + k - 1 >= i:
            return self.quickSelect(A, i, end, k - (i - start))
            
        return A[j + 1]