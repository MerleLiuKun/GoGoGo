/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 //解题思路：递归方法，先比较两个链表头部最小的与剩下元素merge
 先判断两个链表是否非空
 
 */
 package mergeTwoLists
 type ListNode struct {
	 Val int
	 Next *ListNode
 }

 func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{}
	pre := head
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			pre.Next = l2
			l2 = l2.Next
		}else {
			pre.Next =l1
			l1 = l1.Next
		}
		pre =pre.Next
	}
	if l1 == nil {
		pre.Next =l2
	}else {
		pre.Next = l1
	}
	return head.Next
}