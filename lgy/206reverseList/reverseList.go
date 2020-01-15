/*
非递归方法解决反转链表问题
by lgy 2020/1/15

*/

package reverseList
type ListNode struct {
	
	Next *ListNode
}
func reverseList(head *ListNode) *ListNode {
	var pre *ListNode
	var next *ListNode

	for head != nil {
		next = head.Next
		head.Next = pre
		pre = head 
		head = next
	}
	return pre
}
/*
递归方式

*/
func reverseList1(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	newHead := reverseList(head.Next)
	head.Next.Next = head 
	head.Next = nil
	return newHead
}