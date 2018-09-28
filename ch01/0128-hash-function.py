"""
128. 哈希函数
在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）
转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可
以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值
33，假设任何字符串都是基于33的一个大整数，比如：

hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE

其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。

给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。

样例
对于key="abcd" 并且 size=100， 返回 78

说明
对于这个问题，您没有必要设计自己的哈希算法或考虑任何冲突问题，您只需要按照描述实现算法.
"""
class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        ans = 0
        for x in key:
            # print(x)
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        # for i in range(0, len(key)):
        #     ans += ord(key[i]) * pow(33, len(key) - i - 1)
        # ans %= HASH_SIZE
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.hashCode("abcd", 1000))