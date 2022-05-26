# Definition for singly-linked list.
from os import curdir


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        t_head = None
        while head:
            node = ListNode(head.val)
            if t_head:
                node.next = t_head
            t_head = node
            head = head.next

        return t_head

    def reverseList_2(self, head: ListNode) -> ListNode:
        # 核心逻辑如下，多注意 赋值的转换
        prev, cur = None, head
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        return prev


if __name__ == '__main__':
    from ikaros.tools.tree.list_and_singly_linked_list import array_to_slinked_list, slinked_list_to_array

    arr = [1,2]
    head = array_to_slinked_list(arr)

    s = Solution()
    h = s.reverseList(head)
    r = slinked_list_to_array(h)
    print(r)
