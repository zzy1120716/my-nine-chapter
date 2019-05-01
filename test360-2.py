#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def longpath(matrix):
    if not matrix or not matrix[0]:
        return 0
    sequence = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sequence.append((matrix[i][j], i, j))
    sequence.sort()

    check = {}
    for h, x, y in sequence:
        cur_pos = (x, y)
        if cur_pos not in check:
            check[cur_pos] = 1
        cur_path = 0
        for dx, dy in DIRECTIONS:
            if is_valid(x + dx, y + dy, matrix, h):
                cur_path = max(cur_path, check[(x + dx, y + dy)])
        check[cur_pos] += cur_path

    vals = check.values()
    return max(vals)


def is_valid(x, y, matrix, h):
    row, col = len(matrix), len(matrix[0])
    return x >= 0 and x < row and y >= 0 and y < col and matrix[x][y] < h


# ******************************结束写代码******************************


_matrix_rows = 0
_matrix_cols = 0
_matrix_rows = int(input())
_matrix_cols = int(input())

_matrix = []
for _matrix_i in range(_matrix_rows):
    _matrix_temp = list(map(int, re.split(r'\s+', input().strip())))
    _matrix.append(_matrix_temp)

res = longpath(_matrix)

print(str(res) + "\n")

'''
3
3
9 9 4
6 6 8
2 1 1

4
'''