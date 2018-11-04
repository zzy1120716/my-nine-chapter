"""
427. 生成括号
给定 n 对括号，请写一个函数以将其生成新的括号组合，并返回所有组合结果。

样例
给定 n = 3, 可生成的组合如下:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

"""
方法一：暴力法
生成所有 2^(2n)个 '(' 和 ')' 字符构成的序列。然后，我们将检查每一个是否有效。
为了生成所有序列，我们使用递归。长度为 n 的序列就是 '(' 加上所有长度为 n-1 的序列，以及 ')' 加上所有长度为 n-1 的序列。
为了检查序列是否为有效的，我们会跟踪平衡(bal)，也就是左括号的数量减去右括号的数量的净值。如果这个值始终小于零或者不以零结束，
该序列就是无效的，否则它是有效的。
"""
class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


"""
方法二：回溯法
只有在我们知道序列仍然保持有效时才添加 '(' or ')'，而不是像方法一那样每次添加。
我们可以通过跟踪到目前为止放置的左括号和右括号的数目来做到这一点，

如果我们还剩一个位置，我们可以开始放一个左括号。 如果它不超过左括号的数量，我们可以放一个右括号。
"""
class Solution1:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans


"""
方法三：闭合数
为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。

考虑有效括号序列 S 的闭包数：至少存在index> = 0，使得 S[0], S[1], ..., S[2*index+1]是有效的。 显然，每个括号序列都有一个唯一的闭包号。 
我们可以尝试单独列举它们。

对于每个闭合数 c，我们知道起始和结束括号必定位于索引 0 和 2*c + 1。然后两者间的 2*c 个元素一定是有效序列，其余元素一定是有效序列。
"""
class Solution2:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans


"""
方法四：DFS模板
dfs方法中，首先要检查n是否为零
"""
class Solution3:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        self.results = []
        self.dfs('', n, n)
        return self.results

    def dfs(self, S, left, right):
        if not left and not right:
            self.results.append(S)
            return

        if left > 0:
            self.dfs(S + '(', left - 1, right)
        if right > 0 and left < right:
            self.dfs(S + ')', left, right - 1)


if __name__ == '__main__':
    s = Solution3()
    ans = s.generateParenthesis(3)
    print(ans)