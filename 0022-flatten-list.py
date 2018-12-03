"""
22. 平面列表
给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。

样例
给定 [1,2,[1,2]]，返回 [1,2,1,2]。

给定 [4,[3,[2,[1]]]]，返回 [4,3,2,1]。

挑战
请用非递归方法尝试解答这道题。

注意事项
如果给定的列表中的要素本身也是一个列表，那么它也可以包含列表。
"""


class Solution(object):

    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = [nestedList]
        flatten_list = []

        while stack:
            top = stack.pop()
            if type(top) == list:
                for elem in reversed(top):
                    stack.append(elem)
            else:
                flatten_list.append(top)
        return flatten_list


if __name__ == '__main__':
    print(Solution().flatten([1, 2, [1, 2]]))
    print(Solution().flatten([4, [3, [2, [1]]]]))
