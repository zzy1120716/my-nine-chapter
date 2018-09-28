"""
607. Two Sum III - Data structure design
设计b并实现一个 TwoSum 类。他需要支持以下操作:
add 和 find。
add -把这个数添加到内部的数据结构。
find -是否存在任意一对数字之和等于这个值

样例
add(1);add(3);add(5);
find(4)//返回true
find(7)//返回false
"""
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