"""
780. 删除无效的括号
删除最小数目的无效括号，使得输入字符串有效，返回所有可能的结果。

样例
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
注意事项
输入字符串可能包含除括号( 和 )之外的字符。
"""

"""
方法一：回溯法
"""
class Solution:

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float('inf')

    """
    @param string: 递归的原始字符串
    @param index: 原始字符串中的当前索引
    @param left: 目前左括号的数量
    @param right: 目前右括号的数量
    @param expr: 这一次递归的结果表达式
    @param rem_count: 这一次递归删去的括号数量
    """
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        # 如果已经到达string的末尾
        if index == len(string):
            # 如果当前表达式有效。唯一可能无效的场景就是当
            # left > right。另一种方式我们在递归的早期处理。
            if left_count == right_count:
                if rem_count <= self.min_removed:
                    # 这是结果表达式
                    # 字符串在Python中是不可变的，因此我们在递归中移动list
                    # 最终join得到最后的string。
                    possible_ans = "".join(expr)

                    # 如果当前删除括号的数量小于当前最小值，则忽略
                    # 前一个答案并更新当前最小数量。
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)

        else:
            current_char = string[index]

            # 如果当前字符不是括号，只需向前递归一步。
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count)
                expr.pop()
            else:
                # 否则，一次递归就是忽略当前的字符。
                # 所以，我们增加删除的数量，并保持left和right不变
                self.remaining(string, index + 1, left_count, right_count, expr, rem_count + 1)
                expr.append(current_char)

                # 如果当前括号是左括号，我们增加left并向前移动
                if string[index] == '(':
                    self.remaining(string, index + 1, left_count + 1, right_count, expr, rem_count)

                elif right_count < left_count:
                    # 如果当前括号是右括号，我们只考虑如果我们
                    # 有更多的左括号并增加right并向前移动。
                    self.remaining(string, index + 1, left_count, right_count + 1, expr, rem_count)

                expr.pop()

    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        # 重置针对每个测试用例使用的class级变量
        self.reset()

        # 递归调用
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)


"""
方法二：受限的回溯法
"""
class Solution1:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        left = right = 0

        # 首先，找出错位的左右括号的数量
        for char in s:
            # 仅仅记录左边的。
            if char == '(':
                left += 1
            elif char == ')':
                # 如果没有匹配的left，那么这是错位的right，记录它。
                right = right + 1 if left == 0 else right

                # 减少左括号的数量，因为我们已经找到一个right
                # 能够匹配一个left
                left = left - 1 if left > 0 else left

        result = {}

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # 如果到达了字符串结尾，仅检查结果字符串
            # 是否有效，并且我们需要删除的左右括号是否都已经删除了
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    ans = "".join(expr)
                    result[ans] = 1
            else:
                # 丢弃的案例。注意这里是剪枝的条件
                # 我们不继续递归，如果剩余的括号数量为0。
                if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem - (s[index] == '('),
                            right_rem - (s[index] == ')'), expr)

                expr.append(s[index])

                # 仅向前递归一步，如果当前字符不是一个括号
                if s[index] != '(' and s[index] != ')':
                    recurse(s, index + 1,
                            left_count,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == '(':
                    # 考虑一个左括号
                    recurse(s, index + 1,
                            left_count + 1,
                            right_count,
                            left_rem,
                            right_rem, expr)
                elif s[index] == ')' and left_count > right_count:
                    # 考虑一个右括号
                    recurse(s, index + 1,
                            left_count,
                            right_count + 1,
                            left_rem,
                            right_rem, expr)

                # pop用来回溯
                expr.pop()

        # 现在，left和right告诉我们左右括号的错位个数
        # 极大地帮助我们修剪了递归
        recurse(s, 0, 0, 0, left, right, [])
        return list(result.keys())


"""
方法三：易于理解的版本
"""
class Solution2:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        self.ans = set()
        self.min_removed = float("inf")

        def dfs(depth, left, right, removed, cur):
            if depth == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, removed, cur + s[depth])
                else:
                    dfs(depth + 1, left, right, removed + 1, cur)
                    if s[depth] == "(":
                        dfs(depth + 1, left + 1, right, removed, cur + "(")
                    elif s[depth] == ")" and right < left:
                        dfs(depth + 1, left, right + 1, removed, cur + ")")

        dfs(0, 0, 0, 0, "")
        return list(self.ans)


class Solution3:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1

        self.ans = set()

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left_rem == 0 and right_rem == 0:
                    self.ans.add(cur)
            else:
                if s[depth] == "(" and left_rem > 0:
                    dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
                elif s[depth] == "(":
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
                elif s[depth] == ")" and right < left:
                    dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

        dfs(0, 0, 0, left, right, "")
        return list(self.ans)


"""
方法四：BFS
每次往queue里加入当前string, 如果string不满足条件，从左到右移除每个char， 加入下一个level中。
如果在当前level中找到满足条件的string， 在当前level停止。
"""
class Solution4:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        import queue
        q = queue.Queue()
        q.put(s)
        results, visited = [], set()
        visited.add(s)
        isStop = False
        while not q.empty():
            size = q.qsize()
            for k in range(size):
                s = q.get()
                if self.check_valid(s):
                    isStop = True
                    results.append(s)
                if isStop:
                    break
                for i in range(len(s)):
                    if s[i] == "(" or s[i] == ")":
                        new_s = s[:i] + s[i + 1:]
                        if new_s not in visited:
                            q.put(new_s)
                            visited.add(new_s)
        if not results:
            return [""]
        return results

    def check_valid(self, s):
        counter = 0
        for c in s:
            if counter < 0:
                return False
            if c == "(":
                counter += 1
            if c == ")":
                counter -= 1
        return counter == 0


if __name__ == '__main__':
    s = Solution()
    ans = s.removeInvalidParentheses("(a)())()")
    print(ans)