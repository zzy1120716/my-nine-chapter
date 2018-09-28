"""
74. 第一个错误的代码版本
代码库的版本号是从 1 到 n 的整数。某一天，有人提交了
错误版本的代码，因此造成自身及之后版本的代码在单元测
试中均出错。请找出第一个错误的版本号。

你可以通过 isBadVersion 的接口来判断版本号 version 是否
在单元测试中出错，具体接口详情和调用方法请见代码的注释
部分。

样例
给出 n=5

调用isBadVersion(3)，得到false

调用isBadVersion(5)，得到true

调用isBadVersion(4)，得到true

此时我们可以断定4是第一个错误的版本号

挑战
调用 isBadVersion 的次数越少越好

注意事项
请阅读上述代码，对于不同的语言获取正确的调用
isBadVersion 的方法，比如java的调用方式是
SVNRepo.isBadVersion(v)
"""

"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""


class Solution:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        start, end = 1, n
        
        while start + 1 < end:
            mid = (start + end) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        if SVNRepo.isBadVersion(start):
            return start
        elif SVNRepo.isBadVersion(end):
            return end
        return -1