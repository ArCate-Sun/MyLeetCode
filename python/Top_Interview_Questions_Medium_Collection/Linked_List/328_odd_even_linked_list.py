"""
Question:
	Odd Even Linked List
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/784/
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def oddEvenList(self, head: ListNode) -> ListNode:

		odd_head = odd_tail = ListNode(0)
		even_head = even_tail = ListNode(0)

		is_odd = True
		while head:
			if is_odd:
				odd_tail.next = head
				odd_tail = odd_tail.next
			else:
				even_tail.next = head
				even_tail = even_tail.next
			head = head.next
			is_odd = not is_odd

		odd_tail.next = even_head.next
		even_tail.next = None
		result = odd_head.next

		return result



if __name__ == "__main__":

	l = ListNode(1)
	l.next = ListNode(2)
	l.next.next = ListNode(3)
	l.next.next.next = ListNode(4)
	l.next.next.next.next = ListNode(5)

	s = Solution()
	p = s.oddEvenList(l)

	while p:
		print(p.val)
		p = p.next
