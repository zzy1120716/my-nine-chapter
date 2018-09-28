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