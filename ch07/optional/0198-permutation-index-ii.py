"""
198. 排列序号II
给出一个可能包含重复数字的排列，求这些数字的所有排列按字典序排序后该排列在其中的编号。
编号从1开始。

样例
给出排列[1, 4, 2, 2]，其编号为3。
"""

"""
参考例子：32314642

核心点：
1，寻找i位置右侧的比A[i]小的位置时，需要过滤重复值（通过set）
2，计算子排列数量时，首先，要交换i与j位置的值；
然后，要去重复，count = number!/(M1! * M2! * ....* Mn!)，其中Mx是子排列中，某重复值出现的次数
"""


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        # write your code here
        index = 1
        factor = 1
        same_fact = 1
        same_counter = {}
        for i in range(len(A) - 1, -1, -1):
            if A[i] not in same_counter:
                same_counter[A[i]] = 0
            same_counter[A[i]] += 1
            same_fact *= same_counter[A[i]]
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor // same_fact
            factor *= (len(A) - i)
        return index


if __name__ == '__main__':
    ans = Solution().permutationIndexII("32314642")
    print(ans)