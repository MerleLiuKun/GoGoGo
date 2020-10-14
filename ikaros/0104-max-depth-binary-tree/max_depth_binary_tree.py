"""
    递归求得二叉树的深度
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.answer: int = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.loop_depth(root)
        return self.answer

    def loop_depth(self, root: TreeNode, depth: int = 1):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.answer = max(self.answer, depth)

        self.loop_depth(root.left, depth + 1)
        self.loop_depth(root.right, depth + 1)

    def max_depth_simple(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.max_depth_simple(root.left), self.max_depth_simple(root.right)) + 1

    def bfs(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans, arr = 0, []
        arr.append(root)
        while arr:
            size = len(arr)
            while size > 0:
                node = arr.pop(0)
                if node.left is not None:
                    arr.append(node.left)
                if node.right is not None:
                    arr.append(node.right)
                size -= 1
            ans += 1
        return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    right = TreeNode(20)
    right.left = TreeNode(15)
    right.right = TreeNode(7)
    root.right = right

    s = Solution()
    print(s.maxDepth(root))
    print(s.max_depth_simple(root))
    print(s.bfs(root))
