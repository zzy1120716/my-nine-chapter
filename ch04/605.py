"""
605. 序列重构
判断是否序列 org 能唯一地由 seqs重构得出. org是一个由从1到n的
正整数排列而成的序列，1 ≤ n ≤ 10^4。 重构表示组合成seqs的一个
最短的父序列 (意思是，一个最短的序列使得所有 seqs里的序列都是
它的子序列).
判断是否有且仅有一个能从 seqs重构出来的序列，并且这个序列是org。

样例
给定 org = [1,2,3], seqs = [[1,2],[1,3]]
返回 false
解释:
[1,2,3] 并不是唯一可以被重构出的序列，还可以重构出 [1,3,2]

给出 org = [1,2,3], seqs = [[1,2]]
返回 false
解释:
能重构出的序列只有 [1,2].

给定 org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
返回 true
解释:
序列 [1,2], [1,3], 和 [2,3] 可以唯一重构出 [1,2,3].

给定org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
返回 true
"""
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        from collections import defaultdict
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        nodes = set()
        # 构造图的数据结构（邻接链表）
        for seq in seqs:
            # list 转换为 set，与现有的集合求并集
            nodes |= set(seq)
            for i in range(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1
        
        # 取出入度为0的点
        cur = [k for k in indegrees if indegrees[k] == 0]
        res = []
        
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            # 对每一个以现节点为起始的边的终点，入度减1
            for node in edges[cur_node]:
                indegrees[node] -= 1
                # 若此终点入度变为0，则加入到cur中
                if indegrees[node] == 0:
                    cur.append(node)
        
        # 存在2个及以上的入度为0的点，则不存在拓扑排序
        if len(cur) > 1:
            return False
            
        # return len(res) == len(nodes) and res == org
        return res == org