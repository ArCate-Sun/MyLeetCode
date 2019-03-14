"""
Question:
	Intersection of Two Linked Lists
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/107/linked-list/785/
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def getIntersectionNode(self, headA, headB):
		"""
		思路:
			计算链表的长度,
			若两链表相交于某一节点,
			则两链表的尾节点到该相交点的距离相等
		:param headA:
		:param headB:
		:return:
		"""
		len_a = len_b = 0
		node_a = headA
		node_b = headB
		while node_a:
			len_a += 1
			node_a = node_a.next
		while node_b:
			len_b += 1
			node_b = node_b.next
		diff = abs(len_a - len_b)

		node_a = headA
		node_b = headB
		if len_a > len_b:
			while diff:
				node_a = node_a.next
				diff -= 1
		else:
			while diff:
				node_b = node_b.next
				diff -= 1

		while node_a:
			if node_a == node_b:
				return node_a
			node_a = node_a.next
			node_b = node_b.next

		return None

	def getIntersectionNode2(self, headA, headB):
		"""
		思路:
			同时遍历两个链表,
			同时将节点分别加入链表对应的集合,
			遍历过程中检测当前节点是否在对方链表的集合中
		:param headA:
		:param headB:
		:return:
		"""

		node_set_a = set()
		node_set_b = set()
		while headA and headB:
			node_set_a.add(headA)
			node_set_b.add(headB)
			if headB in node_set_a:
				return headB
			elif headA in node_set_b:
				return headA
			headA = headA.next
			headB = headB.next

		while headA:
			if headA in node_set_b:
				return headA
			headA = headA.next
		while headB:
			if headB in node_set_a:
				return headB
			headB = headB.next
		return None



if __name__ == "__main__":

	intersection = ListNode(8)
	intersection.next = ListNode(4)
	intersection.next.next = ListNode(2)

	l1 = ListNode(4)
	l1.next = ListNode(1)
	l1.next.next = intersection

	l2 = ListNode(5)
	l2.next = ListNode(0)
	l2.next.next = ListNode(1)
	l2.next.next.next = intersection

	s = Solution()
	p = s.getIntersectionNode(l1, l2)

	print(p.val)
