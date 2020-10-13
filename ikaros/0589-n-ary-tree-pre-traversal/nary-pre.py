"""
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 递归
    def preorder(self, root: 'Node') -> List[int]:
        if root is Node:
            return []

        rs = [root.val]
        if root.children:
            for r in root.children:
                rs += self.preorder(r)
        return rs

    # 迭代
    def preorder2(self, root: 'Node') -> List[int]:
        stack = [root]
        res = []

        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                if cur.children:
                    for child in cur.children[::-1]:
                        stack.append(child)
        return res


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.children = [n3, n2, n4]
    n3.children = [n5]
    s = Solution()
    print(s.preorder2(n1))
