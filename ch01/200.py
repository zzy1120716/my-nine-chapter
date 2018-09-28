class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        # DP solution
        n = len(s)
        start, end = 0, 0
        result = [[False] * n for i in range(n)]
        
        # Every 1-letter substring is a palindrome
        for i in range(n):
            result[i][i] = True
            
        # 2-letter substring(i, j) is a palindrome if s[i] == s[j]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                result[i][i + 1] = True
                # Change longest palindrome to the first 2-letter palindrome
                if not start and not end:
                    start, end = i, i + 1
        
        # result[i][j] = True if result[i + 1][j - 1] == True and s[i] == s[j]
        for k in range(2, n):
            for i in range(n - 2):
                j = i + k
                # Break the loop if it exceeds the boundaries of the matrix
                if j == n:
                    break
                # Check if current substring is a palindrome
                if result[i + 1][j - 1] and s[i] == s[j]:
                    result[i][j] = True
                    # len(substring(i, j)) > len(substring(x, y))
                    # Always choose first longest palindrome
                    if j - i > end - start:
                        start, end = i, j
        
        return s[start : end + 1]