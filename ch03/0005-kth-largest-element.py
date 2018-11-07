"""
5. 第k大元素
在数组中找到第k大的元素

样例
给出数组 [9,3,2,4,8]，第三大的元素是 4

给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素
是 4，第三大的元素是 3，以此类推

挑战
要求时间复杂度为O(n)，空间复杂度为O(1)

注意事项
你可以交换数组中的元素的位置
"""


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


if __name__ == '__main__':
    print(Solution().kthLargestElement(3, [9, 3, 2, 4, 8]))
