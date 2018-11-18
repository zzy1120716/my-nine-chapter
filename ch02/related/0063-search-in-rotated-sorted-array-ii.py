"""
63. 搜索旋转排序数组 II
跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。

样例
给出[3,4,4,5,7,0,1,2]和target=4，返回 true
"""


# 这个问题在面试中不会让实现完整程序
# 只需要举出能够最坏情况的数据是[1, 1, 1, 1...1] 里有一个0即可。
# 在这种情况下是无法使用二分法的，复杂度是O(n)
# 因此写个for循环最坏也是O(n)，那就写个for循环就好了
# 如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
# 反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return False

        start, end = 0, len(A) - 1

        while start <= end:
            mid = (start + end) // 2

            if A[mid] == target:
                return True

            if A[start] < A[mid]:
                if A[start] <= target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[start] > A[mid]:
                if A[mid] < target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                # if A[start] == A[mid], just move start to the next index.
                # so the worst case, that the array's elements are same, is O(n).
                start += 1

        return False


class Solution1:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return False

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == A[start]:
                start += 1
            elif A[mid] == A[end]:
                end -= 1
            # target is less than A[end] means target is in right part
            elif A[end] >= target:
                # we search from right part
                if A[mid] > A[end]:
                    start = mid
                elif target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # target is in left part
                if A[mid] < target and A[mid] < A[end]:
                    end = mid
                elif A[mid] < target:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return True
        elif A[end] == target:
            return True
        return False