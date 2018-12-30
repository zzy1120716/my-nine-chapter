"""
554. 排序(Map Reduce)
通过Map Reduce框架对整数进行排序

样例
在mapper中， key为可以忽略的文档id， value是待排序的整数.
在reducer中, 你可以指定什么是key或者value(取决于你是如何实现你的mapper类的).
对于输出的reducer类, key可以是任意， 但value需要有序(顺序取决于你什么时候输出)
"""


class SortIntegers:

    # @param {int[]} nums a list of integer
    def mapper(self, _, nums):
        # Write your code here
        # Please use 'yield key, value' here
        for num in nums:
            yield num // 10000, num

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        values.sort()
        yield key, values
