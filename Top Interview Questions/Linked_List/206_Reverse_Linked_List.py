"""
Question:
	Reverse Linked List
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		if not head:
			return head

		prev_node = head
		curr_node = head.next
		prev_node.next = None
		while curr_node:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node
		return prev_node


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
	print_list(head)
	head = s.reverseList(head)
	print_list(head)
