# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(root: TreeNode):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)
        
        stack = helper(root)

        for i in range(1, len(stack)):
            if stack[i] <= stack[i-1]:
                return False
        
        return True


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n2.left = n1
    n2.right = n3

    s = Solution()
    print(s.isValidBST(n2))
