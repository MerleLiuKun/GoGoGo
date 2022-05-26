# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dp = ListNode()
        dp.next = head
        temp = dp
        while temp.next and temp.next.next:
            a = temp.next
            b = temp.next.next
            temp.next = b
            a.next = b.next
            b.next = a
            temp = a
        
        return dp.next
