"""
Question:
	Merge Two Sorted Lists
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""

		end = head = ListNode(None)

		while l1 and l2:
			if l1.val <= l2.val:
				end.next = l1
				end = l1
				l1 = l1.next
			else:
				end.next = l2
				end = l2
				l2 = l2.next

		if l1:
			end.next = l1
		if l2:
			end.next = l2

		return head.next


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

	l1 = create_list([1])
	l2 = create_list([1, 3, 4])
	print("l1:")
	print_list(l1)
	print("l2:")
	print_list(l2)
	head = s.mergeTwoLists(l1, l2)
	print_list(head)
