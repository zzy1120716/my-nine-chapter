"""
182. 删除数字
给出一个字符串 A, 表示一个 n 位正整数, 删除其中 k 位数字, 
使得剩余的数字仍然按照原来的顺序排列产生一个新的正整数。
找到删除 k 个数字之后的最小正整数。
N <= 240, k <= N

样例
给出一个字符串代表的正整数 A 和一个整数 k, 
其中 A = 178542, k = 4
返回一个字符串 "12"
"""
class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        # write your code here
        A = list(A)
        while k > 0:
            flag = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    del A[i]
                    flag = False
                    break
            if flag and len(A) > 1:
                A.pop()
            k -= 1
        while len(A) > 1 and A[0] == '0':
            del A[0]
        return ''.join(A)