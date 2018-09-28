"""
209. 第一个只出现一次的字符
给出一个字符串，找出第一个只出现一次的字符。

样例
对于 "abaccdeff", 'b'为第一个只出现一次的字符.
"""

"""
方法一：Hash
"""
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        counter = {}
        
        for c in str:
            counter[c] = counter.get(c, 0) + 1
        
        for c in str:
            if counter[c] == 1:
                return c

"""
方法二：char list
"""
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        char = [0 for i in range(256)]
        
        for c in str:
            char[ord(c)] += 1
        
        for c in str:
            if char[ord(c)] == 1:
                return c

"""
方法三：Data Stream
"""
class ListCharNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class DataStream:
    def __init__(self, charToPrev={}, dupChars=set()):
        self.charToPrev = charToPrev
        self.dupChars = dupChars
        self.dummy = ListCharNode('.')
        self.tail = self.dummy
        
    def add(self, c):
        if c in self.dupChars:
            return
        
        if c not in self.charToPrev:
            node = ListCharNode(c)
            self.charToPrev[c] = self.tail
            self.tail.next = node
            self.tail = node
            return
        
        # delete the existing node
        prev = self.charToPrev[c]
        prev.next = prev.next.next
        if prev.next is None:
            # tail node removed
            self.tail = prev
        else:
            self.charToPrev[prev.next.val] = prev
        
        self.charToPrev.pop(c)
        self.dupChars.add(c)
    
    def firstUniqueChar(self):
        return self.dummy.next.val


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        ds = DataStream()
        for i in range(len(str)):
            ds.add(str[i])
        
        return ds.firstUniqueChar()
        # if ask for the index
        # return str.find(ds.firstUniqueChar())
