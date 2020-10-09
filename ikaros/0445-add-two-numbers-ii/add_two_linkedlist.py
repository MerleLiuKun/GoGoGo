from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        arr1, arr2 = [], []
        
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        
        ans = None
        carry = 0 # 进位

        while arr1 or arr2 or carry != 0:
            a = 0 if not arr1 else arr1.pop()
            b = 0 if not arr2 else arr2.pop()
            
            c_sum = a + b + carry
            carry = c_sum // 10
            cur_num = c_sum % 10

            c_node = ListNode(cur_num)
            c_node.next = ans
            ans = c_node
        
        return ans
