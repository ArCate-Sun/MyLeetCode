"""
Question:
	Binary Tree Zigzag Level Order Traversal

See:
	https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


# Definition for a binary tree node.
from typing import List


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

		if not root:
			return []

		queue = [root]
		result = []

		positive = True
		while queue:
			level_node_num = len(queue)
			order = []
			for i in range(level_node_num):

				node = queue.pop(0)

				order.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)

			if positive:
				result.append(order)
			else:
				result.append(list(reversed(order)))

			positive = not positive

		return result





if __name__ == "__main__":

	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)

	s = Solution()
	order = s.zigzagLevelOrder(root)
	print(order)