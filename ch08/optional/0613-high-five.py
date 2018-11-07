"""
613. 优秀成绩
每个学生有两个属性 id 和 scores。找到每个学生最高的5个分数的平均值。

样例
给出 results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

返回：
1: 72.40
2: 97.40
"""


# Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score


# 方法一：利用python中的heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        from heapq import heappush, heappop
        from collections import defaultdict

        # defaultdict表示默认value是一个列表
        # 不会出现KeyError异常
        scores = defaultdict(list)

        for record in results:
            # 最小堆
            heappush(scores[record.id], record.score)
            # 大于5个值时，将最小的弹出堆
            if len(scores[record.id]) > 5:
                heappop(scores[record.id])

        avgs = {}
        for key, val in scores.items():
            avgs[key] = sum(val) / 5

        return avgs


# 方法二：每次想插入一个新的成绩，就遍历一次该学生已插入的成绩，把最小的成绩踢出去
class Solution1:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        records = {}
        for r in results:
            if r.id not in records:
                records[r.id] = []

            records[r.id].append(r.score)
            if len(records[r.id]) > 5:
                index = 0
                for i in range(1, 6):
                    if records[r.id][i] < records[r.id][index]:
                        index = i

                records[r.id].pop(index)

        avgs = {}
        for id, scores in records.items():
            avgs[id] = sum(scores) / 5.0

        return avgs


if __name__ == '__main__':
    results = [[1, 91], [1, 92], [2, 93], [2, 99], [2, 98], [2, 97], [1, 60], [1, 58], [2, 100], [1, 61]]
    records = []
    for result in results:
        records.append(Record(result[0], result[1]))
    ans = Solution1().highFive(records)
    print(ans)
