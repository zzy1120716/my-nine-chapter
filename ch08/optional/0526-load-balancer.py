"""
526. 负载均衡器
为网站实现一个负载均衡器，提供如下的 3 个功能：

添加一台新的服务器到整个集群中 => add(server_id)。
从集群中删除一个服务器 => remove(server_id)。
在集群中随机（等概率）选择一个有效的服务器 => pick()。
样例
最开始时，集群中一台服务器都没有。

add(1)
add(2)
add(3)
pick()
>> 1         // 返回值是随机的，这里是 1 或者 2 或者 3 都正确。
pick()
>> 2
pick()
>> 1
pick()
>> 3
remove(1)
pick()
>> 2
pick()
>> 3
pick()
>> 3
"""

# 方法一：直接利用python的set，random中的采样方法random.sample(population, k)，
# 该方法返回随机取出k个数，组成的list
import random


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.servers = set()

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.servers.add(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        self.servers.discard(server_id)

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return random.sample(self.servers, 1)[0] if self.servers else None


# 方法二：官方答案，使用hash存储每个服务器在list中的索引
class LoadBalancer1:
    def __init__(self):
        # do intialization if necessary
        self.server_ids = []
        self.id2index = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.id2index:
            return
        self.server_ids.append(server_id)
        self.id2index[server_id] = len(self.server_ids) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.id2index:
            return

        # remove the server_id
        index = self.id2index[server_id]
        del self.id2index[server_id]

        # overwrite the one to be removed
        last_server_id = self.server_ids[-1]
        self.id2index[last_server_id] = index
        self.server_ids[index] = last_server_id
        self.server_ids.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        index = random.randint(0, len(self.server_ids) - 1)
        return self.server_ids[index]


if __name__ == '__main__':
    lb = LoadBalancer1()
    lb.add(1)
    lb.add(2)
    lb.add(3)
    print(lb.pick())
    print(lb.pick())
    print(lb.pick())
    print(lb.pick())
    lb.remove(1)
    print(lb.pick())
    print(lb.pick())
    print(lb.pick())
