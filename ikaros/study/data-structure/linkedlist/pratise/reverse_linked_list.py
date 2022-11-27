"""
    单链表反转
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"


class Solution:
    def reverse(self, head):

        dp = None
        while head:
            if dp is None:
                dp = Node(head.value)
            else:
                t = Node(head.value)
                t.next = dp
                dp = t
            head = head.next
        
        return dp


if __name__ == '__main__':
    s = Solution()

    head = Node(1, Node(2, Node(3, Node(4))))

    nh = s.reverse(head)

    print(nh)
