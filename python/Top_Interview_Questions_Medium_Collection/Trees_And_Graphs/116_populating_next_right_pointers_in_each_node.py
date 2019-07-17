"""
Question:
	Populating Next Right Pointers in Each Node

See:
	https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a Node.
class Node:
	def __init__(self, val, left, right, next):
		self.val = val
		self.left = left
		self.right = right
		self.next = next


class Solution:
	def connect(self, root: 'Node') -> 'Node':

		if not root:
			return None

		left = curr = root

		while left:
			while curr and curr.left:

				curr.left.next = curr.right

				if curr.next:
					curr.right.next = curr.next.left
					curr = curr.next
				else:
					break

			left = curr = left.left

		return root


if __name__ == "__main__":
	n7 = Node(7, None, None, None)
	n6 = Node(6, None, None, None)
	n5 = Node(5, None, None, None)
	n4 = Node(4, None, None, None)
	n3 = Node(3, n6, n7, None)
	n2 = Node(2, n4, n5, None)
	n1 = Node(1, n2, n3, None)

	s = Solution()
	root = s.connect(n1)
	print(n4.next.val)
