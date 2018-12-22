"""
Question:
	Validate Binary Search Tree
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
"""


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def isValidBST(self, root, min=float('-inf'), max=float('inf')):
		if not root:
			return True
		return min <= root.val <= max and self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)

	def isValidBST2(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""

		if not root:
			return True

		node_stack = [(root, float("-inf"), float("inf"))]

		while node_stack:
			node, left, right = node_stack.pop()
			print(node.val, left, right, right <= node.val, node.val <= left)

			if node.val <= left or node.val >= right:
				return False

			if node.left:
				node_stack.append((node.left, left, node.val))
			if node.right:
				node_stack.append((node.right, node.val, right))

		return True


if __name__ == "__main__":

	s = Solution()

	root = TreeNode(5)
	root.left = TreeNode(1)
	root.right = TreeNode(4)
	root.right.left = TreeNode(3)
	root.right.right = TreeNode(6)
	output = s.isValidBST(root)
	print("Output: %s" % output)

	root = TreeNode(0)
	root.right = TreeNode(-1)
	output = s.isValidBST(root)
	print("Output: %s" % output)