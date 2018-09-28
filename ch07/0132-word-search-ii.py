"""
132. 单词搜索 II
给出一个由小写字母组成的矩阵和一个字典。
找出所有同时在字典和矩阵中出现的单词。一
个单词可以从矩阵中的任意位置开始，可以向左
/右/上/下四个相邻方向移动。一个字母在一个单
词中只能被使用一次。

样例
给出矩阵：

doaf
agai
dcan
和字典：

{"dog", "dad", "dgdg", "can", "again"}

返回 {"dog", "dad", "can", "again"}


dog:
doaf
agai
dcan
dad:

doaf
agai
dcan
can:

doaf
agai
dcan
again:

doaf
agai
dcan
挑战
使用单词查找树来实现你的算法
"""

"""
方法一：哈希表
"""
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []
        
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    result
                )
        
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result
            )
            visited.remove((x_, y_))
        
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

"""
方法二：Trie
"""
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
    
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        
        return node

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []
        
        trie = Trie()
        for word in words:
            trie.add(word)
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result
                )
        
        return list(result)
        
    
    def search(self, board, x, y, node, visited, result):
        if node is None:
            return
        
        if node.is_word:
            result.add(node.word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                node.children.get(board[x_][y_]),
                visited,
                result
            )
            visited.remove((x_, y_))
            
    
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])