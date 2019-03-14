"""
Question:
	Add Two Numbers
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/783/
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""
		思路:
			同时遍历两个链表,
			节点的数值相加,
			生成新的节点,
			并判断是否进位
		:param l1:
		:param l2:
		:return:
		"""

		head = node = ListNode(0)
		carry = 0
		while l1 or l2:

			sum = carry

			if l1:
				sum += l1.val
				l1 = l1.next
			if l2:
				sum += l2.val
				l2 = l2.next

			carry, sum = divmod(sum, 10)
			node.next = ListNode(sum)
			node = node.next

		if carry:
			node.next = ListNode(1)

		return head.next

	def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""
		思路:
			现将列表转换成数字进行运算,
			再将运算结果转为列表
		:param l1:
		:param l2:
		:return:
		"""

		num1 = num2 = 0

		p = l1
		l1 = []
		while p:
			l1.append(p.val)
			p = p.next
		for i in reversed(l1):
			num1 = num1 * 10 + i

		p = l2
		l2 = []
		while p:
			l2.append(p.val)
			p = p.next
		for i in reversed(l2):
			num2 = num2 * 10 + i

		result = num1 + num2

		if result:
			head = node = ListNode(result % 10)
			result //= 10
			while result:
				node.next = ListNode(result % 10)
				result //= 10
				node = node.next
		else:
			head = ListNode(0)

		return head


if __name__ == "__main__":

	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)

	s = Solution()
	p = s.addTwoNumbers(l1, l2)

	while p:
		print(p.val)
		p = p.next
