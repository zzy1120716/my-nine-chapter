class TwoSum:
    
    nums = []
    
    """
    @param: number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        self.nums.append(number)

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        hash = {}
        for i in range(len(self.nums)):
            if value - self.nums[i] in hash:
                return True
            hash[self.nums[i]] = i
        return False