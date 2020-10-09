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
    
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)

        root = head
        carry = 0
        
        while l1 or l2 or carry:
            l1_num = 0
            if l1:
                l1_num = l1.val
                l1 = l1.next
            l2_num = 0
            if l2:
                l2_num = l2.val
                l2 = l2.next
            
            num = carry + l1_num + l2_num
            carry = num // 10
            num = num % 10
            
            root.next = ListNode(num)
            root = root.next
        return head.next
