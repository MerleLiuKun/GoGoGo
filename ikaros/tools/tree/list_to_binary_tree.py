"""
    列表转为二叉树
"""
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"TreeNode(val={self.val},left={self.left},right={self.right})"

def array_to_tree(array: List[Optional[int]]) -> Optional[TreeNode]:
    if not array:
        return None
    root = TreeNode(array[0])
    queue = deque([root])
    length = len(array)
    idx = 1

    while idx < length:
        node = queue.popleft()
        print(node)
        if node:
            if array[idx] is not None:
                node.left = TreeNode(array[idx])
            queue.append(node.left)

            if idx + 1 < length:
                if array[idx + 1] is not None:
                    node.right = TreeNode(array[idx + 1])
                queue.append(node.right)
                idx += 1
            idx += 1

    return root

if __name__ == "__main__":
    arr = [1,None,2,3]
    
    a = array_to_tree(arr)
    print(a)
