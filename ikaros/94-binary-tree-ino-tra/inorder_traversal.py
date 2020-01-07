from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: Optional[int]):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )
    
    def inorderTraversalIter(self, root: TreeNode) -> List[int]:
        """
        按照 左根右 来逐一打入到栈中
        """
        if root is None:
            return []
        
        stack = []
        res = []
        current = root

        # 如果如果
        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current is not None:
                res.append(current.val)
                current = current.right
        
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    right = TreeNode(2)
    root.right = right
    right.left = TreeNode(3)

    s = Solution()
    r = [1,3,2]
    print(r==s.inorderTraversal(root))
    print(r==s.inorderTraversalIter(root))
