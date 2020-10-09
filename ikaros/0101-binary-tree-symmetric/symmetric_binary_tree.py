"""
    判断对称二叉树
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        
        return (left.val == right.val) and self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
    
    def isSymmetricIter(self, root: TreeNode) -> bool:
        if root is None:
            return True

        q: List[TreeNode] = [root.left, root.right]

        while q:
            left = q.pop(0)
            right = q.pop(0)

            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False

            if left.val != right.val:
                return False
            
            q.extend([left.left, right.right])
            q.extend([left.right, right.left])
        
        return True



if __name__ == "__main__":
    root = TreeNode(3)

    left = TreeNode(2)
    left.left = TreeNode(3)
    left.right = TreeNode(4)
    root.left = left

    right = TreeNode(2)
    right.left = TreeNode(4)
    right.right = TreeNode(3)
    root.right = right
    

    s = Solution()
    print(s.isSymmetric(root))
    print(s.isSymmetricIter(root))
