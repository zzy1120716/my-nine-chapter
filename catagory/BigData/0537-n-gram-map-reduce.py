"""
537. N-Gram (Map Reduce)
给出若干字符串和数字 N。用 Map Reduce 的方法统计所有 N-Grams 及其出现次数 。以字母为粒度。

样例
Given N = 3
doc_1: "abcabc"
doc_2: "abcabc"
doc_3: "bbcabc"

The final result should be:

[
  "abc": 5,
  "bbc": 1,
  "bca": 3,
  "cba": 3
]
"""


class NGram:

    # @param {int} n a integer
    # @param {str} string a string
    def mapper(self, _, n, string):
        # Write your code here
        # Please use 'yield key, value' here
        """abcabc"""
        length = len(string)
        for start in range(length - n + 1):
            """
            abc, 1
            bca, 1
            cab, 1
            abc, 1
            """
            yield string[start: start + n], 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        """
        abc, 2
        bca, 1
        cab, 1
        """
        yield key, sum(values)
