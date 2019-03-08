"""
415. 有效回文串
给定一个字符串，判断其是否为一个回文串。只考虑
字母和数字，忽略大小写。

样例
"A man, a plan, a canal: Panama" 是一个回文。

"race a car" 不是一个回文。

挑战
O(n) 时间复杂度，且不占用额外空间。

注意事项
你是否考虑过，字符串有可能是空字符串？这是面试过程中，
面试官常常会问的问题。

在这个题目中，我们将空字符串判定为有效回文。
"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalpha() and not s[i].isdigit():
                i += 1
            while i < j and not s[j].isalpha() and not s[j].isdigit():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
