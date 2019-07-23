"""
Question:
	Serialize and Deserialize Binary Tree
See:
	https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""
import json
from typing import List
from common.verification import Verification


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""

		def tuplify(node):
			if node:
				return [node.val, tuplify(node.left), tuplify(node.right)]
			else:
				return None

		return json.dumps(tuplify(root))

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""

		def detuplify(data):

			if data:
				val, left, right = data
				node = TreeNode(val)
				node.left = detuplify(left)
				node.right = detuplify(right)
				return node
			else:
				return None

		return detuplify(json.loads(data))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
