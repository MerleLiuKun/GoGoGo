"""
    二叉树的前序遍历
"""
from typing import Optional

class TreeNode:
    def __init__(self, x: Optional[int]):
        self.val = x
        self.left = None
        self.right = None
    

class Solution:
    # 递归解法
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + [self.preorderTraversal(root.left)] + [self.preorderTraversal(root.right)]


    def preorderTraversalIter(self, root: TreeNode) -> List[int]:
        """
        按照 前序遍历的 定义， 根左右.
        """
        if root is None:
            return []
        
        stack = [root]
        res = []
        while stack:
            cur_node = stack.pop()

            if cur_node is not None:
                res.append(cur_node.val)

                if cur_node.right is not None:
                    stack.append(cur_node.right)
                if cur_node.left is not None:
                    stack.append(cur_node.left)

        return res
