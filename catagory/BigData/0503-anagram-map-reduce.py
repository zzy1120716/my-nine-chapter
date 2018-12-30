"""
503. 乱序字符串 (Map Reduce版本)
用Map来找乱序字符串的列表

样例
给出["lint", "intl", "inlt", "code"],返回 ["lint", "inlt", "intl"],["code"].

给出 ["ab", "ba", "cd", "dc", "e"], 返回 ["ab", "ba", "cd", "dc"],["e"].
"""


class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value' here

        """lint intl inlt code"""
        for word in line.split():
            """
            ilnt lint
            ilnt intl
            ilnt inlt
            cdeo code
            """
            yield ''.join(sorted(list(word))), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        """
        ilnt, [lint, intl, inlt]
        cdeo, [code]
        """
        yield key, list(values)
