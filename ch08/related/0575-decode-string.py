"""
575. 字符串解码
给出一个表达式 s，此表达式包括数字，字母以及方括号。在方括号前的数字表示方括号内容的重复次数
(括号内的内容可以是字符串或另一个表达式)，请将这个表达式展开成一个字符串。

样例
S = abc3[a] 返回 abcaaa
S = 3[abc] 返回 abcabcabc
S = 4[ac]dy 返回 acacacacdy
S = 3[2[ad]3[pf]]xyz 返回 adadpfpfpfadadpfpfpfadadpfpfpfxyz

挑战
你可以不通过递归的方式完成展开吗？
"""


# 利用两个栈，一个存数，一个存字符串
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        num_stack = []
        str_stack = []

        i = 0
        while i < len(s):
            if s[i].isalpha() or s[i] == '[':
                str_stack.append(s[i])
            # 连续出现数字，应当将多个数字拼接入栈，如‘20’
            if s[i].isdigit():
                num_str = ''
                while i < len(s) and s[i].isdigit():
                    num_str += s[i]
                    i += 1
                num_stack.append(int(num_str))
                i -= 1
            # 遇到‘]’则要进行一次运算
            if s[i] == ']':
                consecutive_str = ''
                num = num_stack.pop(-1)
                while str_stack:
                    top = str_stack.pop(-1)
                    if top == '[':
                        break
                    consecutive_str = top + consecutive_str
                consecutive_str *= int(num)
                # 运算结果放到栈顶
                str_stack.append(consecutive_str)

            i += 1

        # 栈中剩余的元素是多个字符串片段，
        # 将它们连接起来
        return ''.join(str_stack)


# DFS
class Solution1:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ''
        res, pos = self.helper(0, s)
        return res

    def helper(self, pos, s):
        res = ''
        number = 0
        while pos < len(s):
            if s[pos].isdigit():
                number = number * 10 + int(s[pos])
            elif s[pos] == '[':
                substring, pos = self.helper(pos + 1, s)
                res += substring * number
                number = 0
            elif s[pos] == ']':
                return res, pos
            else:
                res += s[pos]
            pos += 1
        return res, pos


# 利用一个栈
class Solution2:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue

            strs = []
            while stack and stack[-1] != '[':
                strs.append(stack.pop())

            # skip '['
            stack.pop()

            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
            stack.append(''.join(reversed(strs)) * repeats)

        return ''.join(stack)


if __name__ == '__main__':
    ans = Solution1().expressionExpand("3[2[ad]3[pf]]xyz")
    print(ans)
    assert ans == 'adadpfpfpfadadpfpfpfadadpfpfpfxyz'

    ans = Solution1().expressionExpand("abc3[a]")
    print(ans)
    assert ans == 'abcaaa'

    ans = Solution1().expressionExpand("4[ac]dy")
    print(ans)
    assert ans == 'acacacacdy'

    ans = Solution1().expressionExpand("3[abc]")
    print(ans)
    assert ans == 'abcabcabc'