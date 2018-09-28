"""
9. Fizz Buzz 问题
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
样例
比如 n = 15, 返回一个字符串数组：

[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]
挑战
Can you do it with only one if statement?
"""
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        results = []
        i, p3, p5 = 1, 1, 1
        
        while i <= n:
            while i < p3 * 3 and i < p5 * 5:
                results.append(str(i))
                i += 1
                
            if i <= n and p3 * 3 == p5 * 5:
                results.append("fizz buzz")
                p3 += 1
                p5 += 1
                i += 1
                continue
            
            while i <= n and p3 * 3 <= i:
                results.append("fizz")
                p3 += 1
                i += 1
            
            while i <= n and p5 * 5 <= i:
                results.append("buzz")
                p5 += 1
                i += 1
            
        return results