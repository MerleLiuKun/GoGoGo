"""
    后序遍历
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: Optional[int]):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


if __name__ == "__main__":
    root = TreeNode(1)
    right = TreeNode(2)
    right.left = TreeNode(3)
    root.right = right

    r = [3,2,1]
    s = Solution()
    print(r==s.postorderTraversal(root))
