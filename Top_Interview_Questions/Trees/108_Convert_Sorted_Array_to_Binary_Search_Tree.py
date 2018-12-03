"""
Question:
	Convert Sorted Array to Binary Search Tree
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		if not nums:
			return None

		idx_mid = (len(nums) - 1) // 2
		root = TreeNode(nums[idx_mid])
		nodes = [(root, 0, idx_mid, len(nums) - 1)]

		while nodes:

			node, idx_left, idx_middle, idx_right = nodes.pop()

			if idx_middle > idx_left:
				idx_mid = (idx_left + idx_middle - 1) // 2
				node.left = TreeNode(nums[idx_mid])
				nodes.append((node.left, idx_left, idx_mid, idx_middle - 1))
			if idx_middle < idx_right:
				idx_mid = (idx_middle + 1 + idx_right) // 2
				node.right = TreeNode(nums[idx_mid])
				nodes.append((node.right, idx_middle + 1, idx_mid, idx_right))

		return root

	def sortedArrayToBST2(self, nums, root=None):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""

		print(nums)

		if not nums:
			return None

		node = TreeNode(nums[len(nums) // 2])
		if not root:
			root = node

		node.left = self.sortedArrayToBST(nums[: len(nums) // 2])
		node.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1 :])

		return root


def print_tree(root):
	values = []
	nodes = [root]

	while nodes:

		node = nodes.pop(0)

		if not node:
			values.append(None)
			if nodes and set(nodes).difference({None}):
				nodes.append(None)
				nodes.append(None)
		else:
			values.append(node.val)
			nodes.append(node.left)
			nodes.append(node.right)

	print(values)


if __name__ == "__main__":
	s = Solution()

	nums = [-10, -3, 0, 5, 9]
	root = s.sortedArrayToBST(nums)
	# print("Output: %s" % output)

	print_tree(root)
