"""
50. 数组剔除元素后的乘积
给定一个整数数组A。
定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。请输出B。

样例
给出A=[1, 2, 3]，返回 B为[6, 3, 2]
"""


# quicker solution
# 给定任意一个点， res[i]  的值应该等于它的左边： res[0..i-1] 与 右边 ：res[i+1 ... len] 乘
# 所以第一次从左向右，把每一个点的 res[0..i-1] 乘完算出来暂存在 res[i] 上。
# 然后再从右边向左边乘，把右边res[i+1 ... len] 累乘完再乘以res[i], 注意这里res[i]上一次循环己经暂存
# 成了res[0..i-1]的值， 所以现在结果正好等于: res[0..i-1] * res[i+1 ... len]。
class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        n = len(nums)
        B = [1] * n
        for i in range(1, n):
            B[i] = B[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            B[i] *= right
            right *= nums[i]
        return B


# intuitive solution
class Solution1:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        B = []
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                res *= nums[j]
            B.append(res)
        return B
