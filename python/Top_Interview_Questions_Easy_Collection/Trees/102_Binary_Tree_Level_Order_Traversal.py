"""
Question:
	Binary Tree Level Order Traversal
See:
	https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""

		if not root:
			return []

		result = []
		tmp_list = []

		nodes = [root]
		left = right = root
		tmp_right = None

		while nodes:

			# print([n.val for n in nodes])
			node = nodes.pop(0)

			print("this node: ", node.val)

			tmp_list.append(node.val)
			if node == right:
				result.append(tmp_list)
				tmp_list = []

			# 寻找下一层中最左边的节点
			if not left or node == left:
				left = node.left if node.left else node.right

			# 寻找下一层中最右边的节点
			if node.right:
				tmp_right = node.right
			elif node.left:
				tmp_right = node.left

			if node == right:
				right = tmp_right

			output = [left.val if left else None, right.val if right else None]
			print(output, tmp_right.val if tmp_right else None)

			if node.left:
				nodes.append(node.left)

			if node.right:
				nodes.append(node.right)

		return result


if __name__ == "__main__":
	s = Solution()

	root = TreeNode(3)
	root.left = TreeNode(9)
	root.right = TreeNode(20)
	root.right.left = TreeNode(15)
	root.right.right = TreeNode(7)
	output = s.levelOrder(root)
	print("Output: %s" % output)
