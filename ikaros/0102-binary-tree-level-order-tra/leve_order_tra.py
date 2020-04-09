from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        current: List[TreeNode] = [root]
        up: List[TreeNode] = []
        res: List[List[int]] = []
        item: List[int] = []

        while current or up:
            if (not current) and up:
                res.append(item)
                item = []
                current = up
                up = []
            now = current.pop(0)
            item.append(now.val)
            if now.left:
                up.append(now.left)
            if now.right:
                up.append(now.right)
        
        if item:
            res.append(item)

        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    right = TreeNode(20)
    right.left = TreeNode(15)
    right.right = TreeNode(7)
    root.right = right
    

    s = Solution()
    print(s.level_order(root))
