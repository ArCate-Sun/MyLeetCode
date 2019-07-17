"""
Question:
	Construct Binary Tree from Preorder and Inorder Traversal

See:
	https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def build(self, preorder, inorder, stop=None):
		if preorder and inorder[0] != stop:
			root = TreeNode(preorder.pop(0))
			root.left = self.build(preorder, inorder, root.val)
			inorder.pop(0)
			root.right = self.build(preorder, inorder, stop)
			return root

	def buildTree(self, preorder, inorder):
		return self.build(preorder, inorder)



if __name__ == "__main__":

	preorder = [3,9,20,15,7]
	inorder = [9,3,15,20,7]
	s = Solution()
	s.buildTree(preorder, inorder)