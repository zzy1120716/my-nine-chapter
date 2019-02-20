"""
212. 空格替换
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入
新的字符，且你得到的是“真实的”字符长度。

你的程序还需要返回被替换后的字符串的长度。

样例
样例 1：

输入：string[] = "Mr John Smith" and length = 13
输出：string[] = "Mr%20John%20Smith" and return 17
解释：
对于字符串 "Mr John Smith"，长度为 13。替换空格之后，参数中的字符串需要变为
"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。
样例 2：

输入：string[] = "LintCode and Jiuzhang" and length = 21
输出：string[] = "LintCode%20and%20Jiuzhang" and return 25
解释：
对于字符串 "LintCode and Jiuzhang"，长度为 21。替换空格之后，参数中的字符串需要变为
"LintCode%20and%20Jiuzhang"，并且把新长度 25 作为结果返回。
挑战
在原字符串(字符数组)中完成替换，不适用额外空间

注意事项
如果使用 Java 或 Python, 程序中请用字符数组表示字符串。
"""


class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if not string:
            return length

        spaces = 0
        for c in string:
            if c == ' ':
                spaces += 1
        new_len = length + spaces * 2
        index = new_len - 1
        for i in range(length - 1, -1, -1):
            if string[i] == ' ':
                string[index] = '0'
                string[index - 1] = '2'
                string[index - 2] = '%'
                index -= 3
            else:
                string[index] = string[i]
                index -= 1
        print(''.join(string))
        return new_len


if __name__ == '__main__':
    actual_string = 'Mr John Smith'
    string = list(actual_string)
    string.extend(([''] * (len(actual_string) * 2)))
    print(string)
    print(Solution().replaceBlank(string, 13))
