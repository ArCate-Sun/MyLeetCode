"""
Question:
	Remove Nth Node From End of List
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		node_list = []
		node = head
		while node:
			node_list.append(node)
			node = node.next
		if n == len(node_list):
			node_list.pop(0)
		else:
			node_list[-n - 1].next = node_list[-n].next

		return node_list[0] if node_list else None

	def removeNthFromEnd2(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		length = 0
		node = head
		while node:
			node = node.next
			length += 1

		if n == length:
			return head.next

		node = head
		for i in range(0, length - n - 1):
			node = node.next

		node.next = node.next.next
		return head


def create_list(nums):
	"""
	Create List
	:type nums: list
	:rtype: ListNode
	"""

	if not nums:
		return None

	head = ListNode(nums[0])
	node = head
	for i in range(1, len(nums)):
		node.next = ListNode(nums[i])
		node = node.next
	return head


def print_list(head):
	"""
	Print List
	:type head: ListNode
	:rtype: None
	"""

	values = []
	node = head
	while node:
		values.append(node.val)
		node = node.next
	print(values)


if __name__ == "__main__":
	s = Solution()

	head = create_list([1, 2, 3, 4, 5])
	n = 3
	print_list(head)
	head = s.removeNthFromEnd(head, n)
	print_list(head)
