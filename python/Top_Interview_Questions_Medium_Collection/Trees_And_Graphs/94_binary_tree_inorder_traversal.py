"""
Question:
	Binary Tree Inorder Traversal

See:
	https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
"""


# Definition for a binary tree node.
from typing import List


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:

	def inorderTraversal(self, root: TreeNode) -> List[int]:
		"""
		中序遍历
		:param root:
		:return:
		"""

		if not root:
			return []

		inorder = [root]
		result = []

		while inorder:
			node = inorder[-1]
			if node.left:
				inorder.append(node.left)
				node.left = None
			elif node.right:
				result.append(node.val)
				inorder.pop()
				inorder.append(node.right)
			else:
				result.append(node.val)
				inorder.pop()

		return result

if __name__ == "__main__":

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(5)
	root.right.right = TreeNode(6)

	s = Solution()
	inorder = s.inorderTraversal(root)
	for v in inorder:
		print(v)