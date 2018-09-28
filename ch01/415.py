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
