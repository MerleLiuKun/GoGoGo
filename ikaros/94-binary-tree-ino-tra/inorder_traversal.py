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

        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current is not None:
                res.append(current.val)
                current = current.right
        
        return res
    
    def inorderTraversalMorris(self, root: TreeNode) -> List[int]:
        res = []
        current = root
        pre = None

        while current:
            if current.left is None:
                # 如果没有左子树, 就把当前节点添加到输出.
                res.append(current.val)
                current = current.right  # 切换到右子树
            else:
                # 如果存在左子树，需要处理
                pre = current.left
                # 找到最右的子节点 用于承载 当前节点
                while pre.right is not None:
                    pre = pre.right
                pre.right = current
                tmp = current
                current = current.left
                # 将当前节点的左子树置空
                tmp.left = None

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
    print(r==s.inorderTraversalMorris(root))
