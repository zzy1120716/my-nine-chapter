"""
123. 单词搜索
给出一个二维的字母板和一个单词，寻找字母板网格中是否存在这个单词。

单词可以由按顺序的相邻单元的字母组成，其中相邻单元指的是水平或者垂直方向相邻。
每个单元中的字母最多只能使用一次。

样例
给出board =
[
  "ABCE",
  "SFCS",
  "ADEE"
]

word = "ABCCED"， ->返回 true,
word = "SEE"，-> 返回 true,
word = "ABCB"， -> 返回 false.
"""


# DFS
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not word:
            return True
        row = len(board)
        col = len(board[0])
        if row == 0 or col == 0:
            return False
        # visited matrix
        visited = [[False for _ in range(col)] for _ in range(row)]
        # DFS
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, x, y):
        if word == '':
            return True
        row = len(board)
        col = len(board[0])
        if x < 0 or x >= row or y < 0 or y >= col:
            return False
        if board[x][y] == word[0] and not visited[x][y]:
            visited[x][y] = True
            # (x - 1, y) and (x + 1, y), and (x, y - 1) and (x, y + 1)
            if self.dfs(board, word[1:], visited, x - 1, y) \
                    or self.dfs(board, word[1:], visited, x + 1, y) \
                    or self.dfs(board, word[1:], visited, x, y - 1) \
                    or self.dfs(board, word[1:], visited, x, y + 1):
                return True
            else:
                visited[x][y] = False
        return False


# 简洁版本 DFS 记忆化搜索， 没有使用整个矩阵，只变化当前位置，判断后再置回
class Solution1:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, x, y, word):
        row = len(board)
        col = len(board[0])
        if len(word) == 0:
            return True
        elif x < 0 or x >= row or y < 0 or y >= col or board[x][y] != word[0]:
            return False

        board[x] = board[x][0:y] + '#' + board[x][y + 1:]
        res = self.dfs(board, x - 1, y, word[1:]) \
            or self.dfs(board, x + 1, y, word[1:]) \
            or self.dfs(board, x, y - 1, word[1:]) \
            or self.dfs(board, x, y + 1, word[1:])
        board[x] = board[x][0:y] + word[0] + board[x][y + 1:]
        return res


if __name__ == '__main__':
    print(Solution1().exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], "ABCCED"))
    print(Solution1().exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], "SEE"))
    print(Solution1().exist([
        "ABCE",
        "SFCS",
        "ADEE"
    ], "ABCB"))
