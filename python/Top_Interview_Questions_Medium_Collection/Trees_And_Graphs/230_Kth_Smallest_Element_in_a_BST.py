"""
Question:
	Kth Smallest Element in a BST

See:
	https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def kthSmallest(self, root: TreeNode, k: int) -> int:

		queue = []
		node = root
		while node:
			queue.append(node)
			node = node.left

		for i in range(1, k):
			# print(i, [n.val for n in queue])
			node = queue.pop()
			if node.right:
				node = node.right
				while node:
					queue.append(node)
					node = node.left

		return queue[-1].val

if __name__ == "__main__":
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)
	n5 = TreeNode(5)
	n6 = TreeNode(6)

	n5.left = n3
	n5.right = n6
	n3.left = n2
	n3.right = n4
	n2.left = n1

	root = n5

	s = Solution()
	result = s.kthSmallest(root, 6)
	print(result)
