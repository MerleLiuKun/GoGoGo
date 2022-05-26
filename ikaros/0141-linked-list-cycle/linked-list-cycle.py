# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针，龟兔赛跑的感觉
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
    
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # 缓存一下节点  O(n * 1)
        cache = set()
        while head:
            if head in cache:
                return True
            cache.add(head)
            head = head.next
        return False
