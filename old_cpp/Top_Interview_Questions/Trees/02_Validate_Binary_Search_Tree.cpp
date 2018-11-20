//
// Validate Binary Search Tree
//
// Required:
// Given a binary tree, determine if it is a valid binary search tree (BST).
// Assume a BST is defined as follows:
//  * The left subtree of a node contains only nodes with keys less than the node's key.
//  * The right subtree of a node contains only nodes with keys greater than the node's key.
//  * Both the left and right subtrees must also be binary search trees.
//
// Example 1:
//     2
//    / \
//   1   3
// Binary tree [2,1,3], return true.
//
// Example 2:
//     1
//    / \
//   2   3
// Binary tree [1,2,3], return false.
//

#include <iostream>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
	/**
	 * 判断树中节点的所有值是否全部大于或小于比较值
	 *
	 * @param root 		根节点
	 * @param num 		比较值
	 * @param isLess 	true	树中所有节点小于比较值
	 * 					false	树中所有节点大于比较值
	 * @return 	true or false
	 */
	bool compareTreeValue(TreeNode *root, int num, bool isLess) {

		if (!root) return true;

		if (isLess ? root->val < num : root->val > num) {
			return this->compareTreeValue(root->left, num, isLess)
				   && this->compareTreeValue(root->right, num, isLess);
		}

		return false;
	}

	/**
	 * 判断是否为二叉排序树
	 *
	 * @param root 		根节点
	 * @return
	 */
	bool isValidBST(TreeNode* root) {

		if (!root) return true;

		if (!this->isValidBST(root->left))
			return false;
		if (!this->isValidBST(root->right))
			return false;

		if (!this->compareTreeValue(root->left, root->val, true))
			return false;
		if (!this->compareTreeValue(root->right, root->val, false))
			return false;

		return true;
	}
};
