"""
    列表转成 单链表
"""
from typing import List, Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None

    def __repr__(self):
        return f"ListNode(val={self.val},next={self.next})"


def array_to_slinked_list(array: List[int]):
    if not array:
        return None
    cur = vir_root = ListNode(0)

    for val in array:
        cur.next = ListNode(val)
        cur = cur.next

    return vir_root.next


def slinked_list_to_array(root: ListNode):
    if not root:
        return []
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res


if __name__ == "__main__":
    arr = [7, 2, 4, 3]

    l1 = array_to_slinked_list(arr)
    print(l1)

    print(slinked_list_to_array(l1))
