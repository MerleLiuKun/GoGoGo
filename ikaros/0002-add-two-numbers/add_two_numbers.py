# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = "", ""

        while l1 or l2:
            if l1:
                s1 = str(l1.val) + s1
                l1 = l1.next

            if l2:
                s2 = str(l2.val) + s2
                l2 = l2.next
        
        r = int(s1) + int(s2)

        root = None
        for n in str(r):
            item = ListNode(n)
            item.next = root
            root = item
        
        return root
        