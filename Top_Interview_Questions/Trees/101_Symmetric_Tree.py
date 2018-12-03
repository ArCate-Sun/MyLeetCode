"""
Question:
	Symmetric Tree
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		if not root:
			return True

		nodes = [root.left, root.right]

		while nodes:

			node_left, node_right = nodes.pop(0), nodes.pop(-1)

			if node_left is None and node_right is None:
				continue

			if not (node_left and node_right):
				return False

			if node_left.val != node_right.val:
				return False

			nodes.insert(0, node_left.right)
			nodes.insert(0, node_left.left)

			nodes.append(node_right.left)
			nodes.append(node_right.right)

		return True


if __name__ == "__main__":
	s = Solution()

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(2)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(4)
	root.right.left = TreeNode(4)
	root.right.right = TreeNode(3)
	output = s.isSymmetric(root)
	print("Output: %s" % output)

	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(2)
	root.left.right = TreeNode(3)
	root.right.right = TreeNode(3)
	output = s.isSymmetric(root)
	print("Output: %s" % output)
