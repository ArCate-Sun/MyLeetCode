"""
Question:
	Maximun Depth of Binary Tree
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
"""


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""

		if not root:
			return 0

		node_stack = [(root, 1)]
		max_depth = 1

		while node_stack:
			node, depth = node_stack.pop()

			max_depth = depth if max_depth < depth else max_depth

			if node.left:
				node_stack.append((node.left, depth + 1))
			if node.right:
				node_stack.append((node.right, depth + 1))

		return max_depth


if __name__ == "__main__":

	s = Solution()

	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	output = s.maxDepth(root)
	print("Output: %s" % output)
