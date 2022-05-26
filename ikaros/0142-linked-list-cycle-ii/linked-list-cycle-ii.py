# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 缓存一下节点  O(n * 1)
        # 但是 这种方式 存储了 N 个节点到 set 里
        cache = set()
        while head:
            if head in cache:
                return head
            cache.add(head)
            head = head.next
        return None

    # 进阶 使用快慢指针操作
    # 首次相遇后, 一方从开始重新出发，再次相遇时 就是起点， 需要点数学知识
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                dec = head  # dec 从起点出发
                while dec is not slow:
                    dec = dec.next
                    slow = slow.next
                return dec
        return None
