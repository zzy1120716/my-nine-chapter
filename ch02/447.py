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