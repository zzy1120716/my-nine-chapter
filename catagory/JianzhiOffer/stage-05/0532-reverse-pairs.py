"""
532. 逆序对
中文English
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
给你一个数组，求出这个数组中逆序对的总数。
概括：如果a[i] > a[j] 且 i < j， a[i] 和 a[j] 构成一个逆序对。

样例
样例1

输入: A = [2, 4, 1, 3, 5]
输出: 3
解释:
(2, 1), (4, 1), (4, 3) 是逆序对
样例2

输入: A = [1, 2, 3, 4]
输出: 0
解释:
没有逆序对
"""
import copy


class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        # write your code here
        if not A:
            return 0
        start, end = 0, len(A) - 1
        tmp = copy.deepcopy(A)
        return self.inverse(tmp, start, end)

    # 1、递归的定义
    def inverse(self, tmp, start, end):
        # 2、递归的出口
        if start == end:
            return 0

        # 3、递归的拆解，分别对左右两边进行递归求值
        mid = (end - start) // 2
        left = self.inverse(tmp, start, start + mid)
        right = self.inverse(tmp, start + mid + 1, end)

        # 本次逆序对数目
        count = 0
        l_right, r_right = start + mid, end
        t = []
        while l_right >= start and r_right >= start + mid + 1:
            if tmp[l_right] > tmp[r_right]:
                t.append(tmp[l_right])
                count += r_right - mid - start
                l_right -= 1
            else:
                t.append(tmp[r_right])
                r_right -= 1
        while l_right >= start:
            t.append(tmp[l_right])
            l_right -= 1
        while r_right >= start + mid + 1:
            t.append(tmp[r_right])
            r_right -= 1
        tmp[start:end + 1] = t[::-1]
        return count + left + right


if __name__ == '__main__':
    print(Solution().reversePairs([2, 4, 1, 3, 5]))
