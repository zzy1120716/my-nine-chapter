"""
829. 字模式 II
给定一个pattern和一个字符串str，查找str是否遵循相同的
模式。
这里遵循的意思是一个完整的匹配，在一个字母的模式和一个
非空的单词str之间有一个双向连接的模式对应。(如果a对应s，
然而b不对应s。例如，给定的模式= "ab"， str = "ss"，返回
false）。

样例
给定模式= "abab"， str = "redblueredblue"，返回true。给
定模式= "aaaa"， str = asdasdasdasd，返回true。给定模式= 
aabb， str = "xyzabcxzyabc"，返回false

注意事项
您可以假设模式和str只包含小写字母
"""
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.is_match(pattern, str, {}, set())
        
    def is_match(self, pattern, str, mapping, used):
        if not pattern:
            return not str
        
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not str.startswith(word):
                return False
            return self.is_match(pattern[1:], str[len(word):], mapping, used)
        
        for i in range(len(str)):
            word = str[:i + 1]
            if word in used:
                continue
            
            used.add(word)
            mapping[char] = word
            
            if self.is_match(pattern[1:], str[i + 1:], mapping, used):
                return True
            
            del mapping[char]
            used.remove(word)
        
        return False