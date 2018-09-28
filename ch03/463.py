class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        if A is None or len(A) == 0:
            return
        
        # write your code here
        for i in range(len(A)):
            for j in range(1, len(A) - i):
                if A[j - 1] > A[j]:
                    A[j - 1], A[j] = A[j], A[j - 1]