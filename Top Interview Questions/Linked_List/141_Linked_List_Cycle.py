"""
Question:
	Linked List Cycle
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):

	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False

	def hasCycle2(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		if not head:
			return False

		node_set = set()
		while head:
			if head in node_set:
				return True
			node_set.add(head)
			head = head.next
		return False
