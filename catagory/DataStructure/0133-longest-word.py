"""
133. 最长单词
给一个词典，找出其中所有最长的单词。

样例
在词典
{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]

在词典
{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]

挑战
遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？
"""


# 遇到更长的单词，就将结果list清空，重新记录，
# 否则，就不断在后面添加长度相等的单词
class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        # write your code here
        ret = []
        max_len = 0
        for word in dictionary:
            if len(word) == max_len:
                ret.append(word)
            elif len(word) > max_len:
                ret = [word]
                max_len = len(word)
        return ret


if __name__ == '__main__':
    print(Solution().longestWords(["dog",
                                   "google",
                                   "facebook",
                                   "internationalization",
                                   "blabla"]))
