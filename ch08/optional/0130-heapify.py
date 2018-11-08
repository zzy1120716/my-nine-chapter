"""
130. 堆化
给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

对于堆数组A，A[0]是堆的根，并对于每个A[i]，A [i * 2 + 1]是A[i]的左儿子并且A[i * 2 + 2]
是A[i]的右儿子。

样例
给出 [3,2,1,4,5]，返回[1,2,3,4,5] 或者任何一个合法的堆数组

挑战
O(n)的时间复杂度完成堆化

说明
什么是堆？

堆是一种数据结构，它通常有三种方法：push， pop 和 top。其中，“push”添加新的元素进入堆，
“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。
什么是堆化？

把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到
A[i * 2 + 1] >= A[i]和A[i * 2 + 2] >= A[i]

如果有很多种堆化的结果？
返回其中任何一个。
"""

# 方法一：trick
import heapq


class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        heapq.heapify(A)


# 方法二：调整堆
class Solution1:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(1, len(A)):
            j = i
            while (j - 1) // 2 >= 0 and A[j] < A[(j - 1) // 2]:
                A[j], A[(j - 1) // 2] = A[(j - 1) // 2], A[j]
                j = (j - 1) // 2


# 方法三：官方答案
# Version 1: this cost O(n)
class Solution2:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, k):
        while k < len(A):
            smallest = k
            if k * 2 + 1 < len(A) and A[k * 2 + 1] < A[smallest]:
                smallest = k * 2 + 1
            if k * 2 + 2 < len(A) and A[k * 2 + 2] < A[smallest]:
                smallest = k * 2 + 2
            if smallest == k:
                break
            A[smallest], A[k] = A[k], A[smallest]
            k = smallest


# Version 2: This cost O(nlogn)
class Solution3:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.siftup(A, i)

    def siftup(self, A, k):
        while k != 0:
            father = (k - 1) // 2
            if A[k] > A[father]:
                break
            A[k], A[father] = A[father], A[k]
            k = father


if __name__ == '__main__':
    A = [3, 2, 1, 4, 5]
    Solution1().heapify(A)
    print(A)
