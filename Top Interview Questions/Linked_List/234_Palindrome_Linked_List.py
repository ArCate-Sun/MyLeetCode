"""
Question:
	Palindrome Linked List
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
"""


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""

		values = []
		slow = fast = head
		while fast and fast.next:
			values.append(slow.val)
			slow = slow.next
			fast = fast.next.next
		if fast:
			slow = slow.next
		for i in range(1, len(values) + 1):
			if values[-i] != slow.val:
				return False
			slow = slow.next
		return True


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

	head = create_list([1, 2])
	print("head:")
	print_list(head)
	print("result:")
	result = s.isPalindrome(head)
	print(result)

	head = create_list([1, 2, 2, 1])
	print("head:")
	print_list(head)
	print("result:")
	result = s.isPalindrome(head)
	print(result)
