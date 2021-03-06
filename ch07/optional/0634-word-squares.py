"""
634. 单词矩阵
给出一系列 不重复的单词，找出所有用这些单词能构成的 单词矩阵。
一个有效的单词矩阵是指, 如果从第 k 行读出来的单词和第 k 列读出来的单词相同
(0 <= k < max(numRows, numColumns))，那么就是一个单词矩阵.
例如，单词序列为 ["ball","area","lead","lady"] ,构成一个单词矩阵。因为对于
每一行和每一列，读出来的单词都是相同的。

b a l l
a r e a
l e a d
l a d y
样例
给出单词序列 ["area","lead","wall","lady","ball"]
返回 [["wall","area","lead","lady"],["ball","area","lead","lady"]]
输出包含 两个单词矩阵，这两个矩阵的输出的顺序没有影响(只要求矩阵内部有序)。

给出单词序列 ["abat","baba","atan","atal"]
返回 [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
输出包含 两个单词矩阵，这两个矩阵的输出的顺序没有影响(只要求矩阵内部有序)。

注意事项
现在至少有一个单词并且不多于1000个单词
所有的单词都有相同的长度
单词的长度最短为 1 最长为 5
每一个单词均由小写字母组成
"""


# define data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return
        return node

    def words_prefix(self, prefix):
        node = self.find(prefix)
        return [] if not node else node.word_list


class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        # 初始化trie，加入单词
        trie = Trie()
        for word in words:
            trie.add(word)
        # 检测是否可以加入，square为list
        squares = []
        for word in words:
            self.search(trie, [word], squares)

        return squares

    def search(self, trie, square, squares):
        # eg. ['wall', 'area'], n: 单词长度 4, pos: 单词数目 2
        n, pos = len(square[0]), len(square)
        # 递归出口 - 需要deep copy
        if n == pos:
            squares.append(list(square))
            return

        # 剪枝 - 以后面为前缀的是否存在
        for col in range(pos, n):
            prefix = ''.join(square[i][col] for i in range(pos))
            if not trie.find(prefix):
                return

        # ['wall', 'area']
        # prefix = 'le'，下一个应该以le开头，每行的pos - 2
        prefix = ''.join(square[i][pos] for i in range(pos))
        for word in trie.words_prefix(prefix):
            # 尝试将word加入
            square.append(word)
            self.search(trie, square, squares)
            # backtracking
            square.pop()


if __name__ == '__main__':
    ans = Solution().wordSquares(["abat", "baba", "atan", "atal"])
    print(ans)