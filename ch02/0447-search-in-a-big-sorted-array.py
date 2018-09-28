"""
447. 在大数组中查找
给一个按照升序排序的正整数数组。这个数组很大以至于你
只能通过固定的接口 ArrayReader.get(k) 来访问第k个数。
(或者C++里是ArrayReader->get(k))，并且你也没有办法
得知这个数组有多大。找到给出的整数target第一次出现
的位置。你的算法需要在O(logk)的时间复杂度内完成，
k为target第一次出现的位置的下标。

如果找不到target，返回-1。

样例
给出 [1, 3, 6, 9, 21, ...], and target = 3, return 1.

给出 [1, 3, 6, 9, 21, ...], and target = 4, return -1.

挑战
O(log k)的时间复杂度，k是target第一次出现的下标。

注意事项
如果你访问了 ArrayReader 中一个不可访问的下标（比如越界），
ArrayReader 会返回 MAXINT = 2,147,483,647。
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 0
        
        while reader.get(index) < target:
            index = index * 2 + 1
            
        start, end = 0, index
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid
                
        if reader.get(start) == target:
            return start
        
        if reader.get(end) == target:
            return end
        
        return -1